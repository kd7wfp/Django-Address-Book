from django.db import models

# Create your models here.
class AB_User(models.Model):
    username = models.CharField(max_length=32,unique=True,null=False,primary_key=True)
    password = models.CharField(max_length=32)
    def __str__(self):
        return self.username