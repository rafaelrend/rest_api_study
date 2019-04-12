from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from first.quickstart.serializers import UserSerializer, GroupSerializer, BookSerializer, FilesSerializer
from first.quickstart.models import Book, Files
from rest_framework.parsers import FileUploadParser
from django.core.files.base import ContentFile
import os
import base64

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