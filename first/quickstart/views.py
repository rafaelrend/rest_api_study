from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from first.quickstart.serializers import UserSerializer, GroupSerializer, BookSerializer, FilesSerializer
from first.quickstart.models import Book, Files, Item
from rest_framework.parsers import FileUploadParser
from django.core.files.base import ContentFile
import os
import base64
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#from django.shortcuts import render

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BOOKS to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# https://stackoverflow.com/questions/20473572/django-rest-framework-file-upload
class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    def perform_create(self, serializer):
        file = self.request.FILES['fileblob']
        # STATIC_ROOT + os.sep +
        destination = open( os.path.join("static" , file.name) , 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
            destination.close()
            
        # obtendo o array de bytes.
        filebytes =  open(os.path.join("static" , file.name), "rb").read()   
        #filebytes =  ContentFile(  os.path.join("static" , file.name)  )
        
        # Include the owner attribute directly, rather than from request data.
        instance = serializer.save( filebyte = base64.encodestring( filebytes ),
                                    name = file.name,
                                    file_content_type = file.content_type,
                                    size = file.size,
                                    id_registry = self.request.data["id_registry"],
                                    table = self.request.data["table"])

class ItemsView:
    # https://www.w3schools.com/python/python_json.asp
    @csrf_exempt
    def save_items(request):
        #request.GET['username']
        #request.POST['username']


        if request.method == 'GET':
            data2 = {"success": "false", "msg": "Chame esse metodo como POST"}
            return JsonResponse(data2)


        text = request.POST['json']
        lista = json.loads(text)
        qtde = len(lista)
        inserted  = 0
        updated = 0

        #insert_list = []
        #update_list = []

        '''
        data = {"results": {
            "qtde": qtde,
            "inserted": inserted,
            "lista": repr(lista)
        }}
        return JsonResponse(data)
        '''
        for item_it in lista:
            obj = Item()

            if 'id' in  item_it and item_it["id"] is not None:
                obj = Item.objects.get(id= item_it["id"] )
                updated +=1
            else:
                inserted += 1

            obj.name = item_it["name"]
            obj.size  = item_it["size"]

            obj.save()

            #insert_many and update_many

        #poll = get_object_or_404(Poll, pk=pk)

        data = {"results": {
            "updated": updated,
            "inserted": inserted
        }}
        return JsonResponse(data)
    
    @csrf_exempt
    def get_cep_description (request, cep):
        
        if cep is None:
            data2 = {"success": "false", "msg": "CEP Vazio"}
            return JsonResponse(data2)
        
        # http://docs.python-requests.org/en/master/
        url = 'http://viacep.com.br/ws/'+cep+'/json/'
        
        r = requests.get(url)
        
        return JsonResponse( r.json() )