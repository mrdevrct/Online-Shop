from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    name_lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    national_code = models.CharField(max_length=100)
