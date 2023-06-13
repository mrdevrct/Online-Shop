from django.db import models

#user
class Users(models.Model):
    username = models.CharField(max_length=255, default='N/A')
    name_lastname = models.CharField(max_length=255, default='N/A')
    password = models.CharField(max_length=255, default='N/A')
    email = models.EmailField(max_length=255, default='N/A')
    phone_number = models.CharField(max_length=255, default='N/A')
    city = models.CharField(max_length=255, default='N/A')
    address = models.CharField(max_length=255, default='N/A')
    national_code = models.CharField(max_length=255, default='N/A')


#product
class Products(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category = models.ForeignKey('Categorys',on_delete=models.CASCADE)



# category
class Categorys(models.Model):
    category_name = models.CharField(max_length=255)
    category_description = models.CharField(max_length=255)
    category_image = models.CharField(max_length=255)


#order
class Orders (models.Model):
    user= models.ForeignKey('Users',on_delete=models.CASCADE)
    order_data = models.CharField(max_length=255)
    total_amount = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    def __str__(self):
        return f'Orders #{self.id}'

#order_details
class orderDetails (models.Model):
    oredr = models.ForeignKey('Orders',on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_notes = models.CharField(max_length=255)
    item_price = models.CharField(max_length=255)
    item_discount =models.CharField(max_length=255)
    item_total = models.CharField(max_length=255)
    item_status = models.CharField(max_length=255)
    def __str__(self):
        return f'orderDetails #{self.id}'

class Carts (models.Model) :
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'Carts #{self.id}'