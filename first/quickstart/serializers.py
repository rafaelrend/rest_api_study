from django.contrib.auth.models import User, Group
from rest_framework import serializers
from first.quickstart.models import Book, Files


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description','isbn','stock','author_id','price','editor','created_at','updated_at','date_release')

class FilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Files
        fields = ( 'name', 'fileblob','filebyte', 'file_content_type','id_registry','table')
