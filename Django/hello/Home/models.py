from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    phone= models.CharField(max_length=12)
    message= models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.name