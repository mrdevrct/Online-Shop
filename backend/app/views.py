from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import Users
from .models import Products
from .models import Categorys
from .models import Orders
from .models import orderDetails
from .models import Carts


# User
@api_view(['GET'])
def dataUsers(request):
    usersList = Users.objects.all()

    data = []
    for user in usersList:
        userData = {
            'nameLastname': user.nameLastname,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'phoneNumber': user.phoneNumber,
            'city': user.city,
            'address': user.address,
            'nationalCode': user.nationalCode
        }
        data.append(userData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def addUser(request):
    data = json.loads(request.body)
    nameLastname = data['nameLastname']
    username = data['username']
    password = data['password']
    email = data['email']
    phoneNumber = data['phoneNumber']
    city = data['city']
    address = data['address']
    nationalCode = data['nationalCode']

    user = Users(
    username = nameLastname,
    name_lastname = username,
    password = password,
    email = email,
    phone_number = phoneNumber,
    city = city,
    address = address,
    national_code = nationalCode,
    )
    user.save()

    return Response({'status': 'ok'})

@api_view(['DELETE'])
def deleteUser(request):
    data = json.loads(request.body)
    userId = data['id']

    Users.objects.filter(id=userId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateUser(request):
    data = json.loads(request.body)
    userId = data['id']
    nameLastname = data['nameLastname']
    username = data['username']
    password = data['password']
    email = data['email']
    phoneNumber = data['phoneNumber']
    city = data['city']
    address = data['address'] 
    nationalCode = data['nationalCode']

    user = Users.objects.get(id=userId)
    username = username,
    nameLastname = nameLastname,
    password = password,
    email = email,
    phoneNumber = phoneNumber,
    city = city,
    address = address,
    nationalCode = nationalCode,
    user.save()

    return JsonResponse({'status': 'ok'})



# Product
@api_view(['GET'])
def dataProduct(request):
    productList = Products.objects.all()

    data = []
    for product in productList:
        productData = {
            'product_name': product.product_name,
            'description': product.description,
            'price' :product.price,
            'image' : product.image,
            'category_id' : product.category_id
        }
        data.append(productData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def addProduct(request):
    data = json.loads(request.body)
    product_name = data['product_name']
    description = data['description']
    price = data['price']
    image = data['image']
    category_id = data['category_id']

    product = Products(
    product_name = product_name,
    description = description,
    price = price,
    image = image,
    category_id = category_id
    )
    product.save()

    return Response({'status': 'ok'})


@api_view(['DELETE'])
def deleteProduct(request):
    data = json.loads(request.body)
    productId = data['id']

    Products.objects.filter(id=productId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateProduct(request):
    data = json.loads(request.body)
    productId = data['id']
    product_name = data['product_name']
    description = data['description']
    price = data['price']
    image = data['image']
    category_id = data['category_id']

    product = Products.objects.get(id=productId)
    product.product_name = product_name
    product.description = description
    product.price = price
    product.image = image
    product.category_id = category_id

    product.save()

    return JsonResponse({'status': 'ok'})



# Category
@api_view(['GET'])
def dataCategory(request):
    categoryList = Categorys.objects.all()
    data = []
    for category in categoryList:
        categoryData = {
            'category_name': category.category_name,
            'category_description': category.category_description,
            'category_image' :category.category_image
        }
        data.append(categoryData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def addCategory(request):
    data = json.loads(request.body)
    category_name = data['category_name']
    category_description = data['category_description']
    category_image = data['category_image']


    category = Categorys(
    category_name = category_name,
    category_description = category_description,
    category_image = category_image,
    )
    category.save()

    return Response({'status': 'ok'})


@api_view(['DELETE'])
def deleteCategory(request):
    data = json.loads(request.body)
    categoryId = data['id']

    Categorys.objects.filter(id=categoryId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateCategory(request):
    data = json.loads(request.body)
    categoryId = data['id']
    category_name = data['category_name']
    category_description = data['category_description']
    category_image = data['category_image']

    category = Categorys.objects.get(id=categoryId)
    category.category_name = category_name
    category.category_description = category_description
    category.category_image = category_image

    category.save()

    return JsonResponse({'status': 'ok'})


# Order
@api_view(['GET'])
def dataOrder(request):
    orderList = Orders.objects.all()

    data = []
    for order in orderList:
        orderData = {
            'user': order.user,
            'order_data': order.order_data,
            'total_amount': order.total_amount,
            'payment_type': order.payment_type,
            'status': order.status

        }
        data.append(orderData)

    return JsonResponse({'data': data})



@api_view(['POST'])
def addOrder(request):
    data = json.loads(request.body)
    user = data['user']
    order_data = data['order_data']
    total_amount = data['total_amount']
    payment_type = data['payment_type']
    status = data['status']

    order = Orders(
    user = user,
    order_data = order_data,
    total_amount = total_amount,
    payment_type = payment_type,
    status = status,
    )
    order.save()

    return Response({'status': 'ok'})

@api_view(['DELETE'])
def deleteOrder(request):
    data = json.loads(request.body)
    orderId = data['id']

    Orders.objects.filter(id=orderId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateOrder(request):
    data = json.loads(request.body)
    orderId = data['id']
    user = data['user']
    order_data = data['order_data']
    total_amount = data['total_amount']
    payment_type = data['payment_type']
    status = data['status']

    order = Orders.objects.get(id=orderId)
    order.user = user
    order.order_data = order_data
    order.total_amount = total_amount
    order.payment_type = payment_type
    order.status = status

    order.save()

    return JsonResponse({'status': 'ok'})



# Cart
@api_view(['GET'])
def dataCart(request):
    cartList = Carts.objects.all()

    data = []
    for cart in cartList:
        cartData = {
            'user': cart.user,
            'product': cart.product,
            'quantity': cart.quantity,
            'status': cart.status
        }
        data.append(cartData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def addCart(request):
    data = json.loads(request.body)
    user = data['user']
    product = data['product']
    quantity = data['quantity']
    status = data['status']

    cart = Carts(
    user = user,
    product = product,
    quantity = quantity,
    status = status
    )
    cart.save()
    return Response({'status': 'ok'})

@api_view(['DELETE'])
def deleteCart(request):
    data = json.loads(request.body)
    cartId = data['id']

    Carts.objects.filter(id=cartId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateCart(request):
    data = json.loads(request.body)
    cartId = data['id']
    user = data['user']
    product = data['product']
    quantity = data['quantity']
    status = data['status']

    cart = Carts.objects.get(id=cartId)
    cart.user = user
    cart.product = product
    cart.quantity = quantity
    cart.status = status

    cart.save()

    return JsonResponse({'status': 'ok'})



# orderDetails
@api_view(['GET'])
def dataOrderDetails(request):
    OrderDetailsList = orderDetails.objects.all()

    data = []
    for orderDetail in OrderDetailsList:
        orderDetailsData = {
            'oredr': orderDetail.oredr,
            'product': orderDetail.product,
            'quantity': orderDetail.quantity,
            'item_notes': orderDetail.item_notes,
            'item_price': orderDetail.item_price,
            'item_discount': orderDetail.item_discount,
            'item_total': orderDetail.item_total,
            'item_status': orderDetail.item_status
        }
        data.append(orderDetailsData)

    return JsonResponse({'data': data})


@api_view(['POST'])
def addOrderDetails(request):
    data = json.loads(request.body)
    oredr = data['oredr']
    product = data['product']
    quantity = data['quantity']
    item_notes = data['item_notes']
    item_price = data['item_price']
    item_discount = data['item_discount']
    item_total = data['item_total']
    item_status = data['item_status']

    orderdetail = orderDetails(
    oredr = oredr,
    product = product,
    quantity = quantity,
    item_notes = item_notes,
    item_price = item_price,
    item_discount = item_discount,
    item_total = item_total,
    item_status = item_status
    )
    orderdetail.save()

    return Response({'status': 'ok'})

@api_view(['DELETE'])
def deleteOrderDetails(request):
    data = json.loads(request.body)
    orderdetailId = data['id']

    orderDetails.objects.filter(id=orderdetailId).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updateOrderDetails(request):
    data = json.loads(request.body)
    orderdetailId = data['id']
    oredr = data['oredr']
    product = data['product']
    quantity = data['quantity']
    item_notes = data['item_notes']
    item_price = data['item_price']
    item_discount = data['item_discount']
    item_total = data['item_total']
    item_status = data['item_status']

    orderdetail = orderDetails.objects.get(id=orderdetailId)
    orderdetail.user = oredr
    orderdetail.product = product
    orderdetail.quantity = quantity
    orderdetail.item_notes = item_notes
    orderdetail.item_price = item_price
    orderdetail.item_discount = item_discount
    orderdetail.item_total = item_total
    orderdetail.item_status = item_status

    orderdetail.save()

    return JsonResponse({'status': 'ok'})