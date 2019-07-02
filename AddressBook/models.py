from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    street_address = models.CharField(max_length=200)
    def __str__(self):
        return self.email
