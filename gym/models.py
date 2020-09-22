from django.db import models

# Create your models here.
class Contact(models.Model):
   
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length =70)
    phone = models.IntegerField()
    msg = models.CharField(max_length=400)


    def __str__(self):
        return self.name



    


    