from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    name_lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    national_code = models.CharField(max_length=255)
