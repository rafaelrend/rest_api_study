from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

# https://www.digitalocean.com/community/tutorials/how-to-create-django-models
# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    stock =  models.CharField(max_length=5, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=18, blank=True, null=True)
    editor = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_release = models.DateTimeField(auto_now_add=False, blank=True, null=True)

#    @models.permalink
#    def get_absolute_url(self):
#         return ('blog_post_detail', (),
#              {
#                 'slug': self.slug,
#              })
    def save(self, *args, **kwargs):
        if not self.id:
             self.created_at = datetime.datetime.now()
        else:
             self.updated_at = datetime.datetime.now()
            
        super(Book, self).save(*args, **kwargs)
        



class Files(models.Model):
        
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    #vou deixar um campo FileField para facilitar a usar a própria tela do django nos testes.. mas não é necessário pra salvar o array de bytes.
    fileblob = models.FileField(blank=True, null=True)
    # aqui vou salvar um base64, porque quero ver como fica.
    filebyte = models.TextField(blank=True, null=True)
    file_content_type = models.CharField(max_length=500, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    id_registry = models.IntegerField(blank=True, null=True)
    table = models.CharField(max_length=500, blank=True, null=True)
    
    '''
    _fileblob = models.TextField(
            db_column='fileblob',
            blank=True , null=True)

    def set_fileblob(self, data):
        self._fileblob = base64.encodestring(data)

    def get_fileblob(self):
        #try:
        #    return base64.decodestring(self._fileblob)
        #except:
            return self._fileblob
        

    fileblob = property(get_fileblob, set_fileblob)
    '''
    class Meta:
         db_table = "files"
         
         
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    createt_at = models.DateTimeField(auto_now_add=True, null=True)
