from django.db import models

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    createt_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
         db_table = "items"