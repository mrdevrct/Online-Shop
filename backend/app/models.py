from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255, default='N/A')
    name_lastname = models.CharField(max_length=255, default='N/A')
    password = models.CharField(max_length=255, default='N/A')
    email = models.EmailField(max_length=255, default='N/A')
    phone_number = models.CharField(max_length=255, default='N/A')
    city = models.CharField(max_length=255, default='N/A')
    address = models.CharField(max_length=255, default='N/A')
    national_code = models.CharField(max_length=255, default='N/A')


# class Product(models.Model):
#     product_name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     price = models.CharField(max_length=255)
#     image = models.CharField(max_length=255)
#     category_id = models.CharField(max_length=255)



# class Categorys(models.Model):
#     category_name = models.CharField(max_length=255)
#     category_description = models.CharField(max_length=255)
#     category_image = models.CharField(max_length=255)