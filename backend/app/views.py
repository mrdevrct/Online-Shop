from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import Users

#user

@api_view(['GET'])
def dataUsers(request):
    usersList = Users.objects.all()

    data = []
    for user in usersList:
        userData = {
            'username': user.username,
            'password': user.password
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

# @api_view(['DELETE'])
# def deleteUser(request):
#     data = json.loads(request.body)
#     userId = data['id']

#     Users.objects.filter(id=userId).delete()

#     return JsonResponse({'status': 'ok'})


# @api_view(['PUT'])
# def updateUser(request):
#     data = json.loads(request.body)
#     userId = data['id']
#     firstname = data['username']
#     lastname = data['lastname']

#     user = Users.objects.get(id=userId)
#     user.firstname = firstname
#     user.lastname = lastname
#     user.save()

#     return JsonResponse({'status': 'ok'})

#Product

# @api_view(['GET'])
# def dataProduct(request):
#     productList = Product.objects.all()

#     data = []
#     for product in productList:
#         productData = {
#             'product_name': product.product_name,
#             'description': product.description,
#             'price' :product.price,
#             'image' : product.image,
#             'category_id' : product.category_id
#         }
#         data.append(productData)

#     return JsonResponse({'data': data})


# @api_view(['POST'])
# def dataProduct(request):
#     data = json.loads(request.body)
#     product_name = data['product_name']
#     description = data['description']
#     price = data['price']
#     image = data['image']
#     category_id = data['category_id']


#     product = Product(
#     product_name = product_name,
#     description = description,
#     price = price,
#     image = image,
#     category_id = category_id
#     )
#     product.save()

#     return Response({'status': 'ok'})


# @api_view(['DELETE'])
# def deleteProduct(request):
#     data = json.loads(request.body)
#     productId = data['id']

#     Product.objects.filter(id=productId).delete()

#     return JsonResponse({'status': 'ok'})


# @api_view(['PUT'])
# def updateProduct(request):
#     data = json.loads(request.body)
#     productId = data['id']
#     product_name = data['product_name']
#     description = data['description']
#     price = data['price']
#     image = data['image']
#     category_id = data['category_id']

#     product = Product.objects.get(id=productId)
#     product.product_name = product_name
#     product.description = description
#     product.price = price
#     product.image = image
#     product.category_id = category_id

#     product.save()

#     return JsonResponse({'status': 'ok'})







#Category
# @api_view(['GET'])
# def dataCategory(request):
#     categoryList = Category.objects.all()

#     data = []
#     for category in categoryList:
#         categoryData = {
#             'category_name': category.category_name,
#             'category_description': category.category_description,
#             'category_image' :category.category_image
#         }
#         data.append(categoryData)

#     return JsonResponse({'data': data})


# @api_view(['POST'])
# def addCategory(request):
#     data = json.loads(request.body)
#     category_name = data['category_name']
#     category_description = data['category_description']
#     category_image = data['category_image']


#     category = Category(
#     category_name = category_name,
#     category_description = category_description,
#     category_image = category_image,
#     )
#     category.save()

#     return Response({'status': 'ok'})


# @api_view(['DELETE'])
# def deleteCategory(request):
#     data = json.loads(request.body)
#     categoryId = data['id']

#     Category.objects.filter(id=categoryId).delete()

#     return JsonResponse({'status': 'ok'})


# @api_view(['PUT'])
# def updateCategory(request):
#     data = json.loads(request.body)
#     categoryId = data['id']
#     category_name = data['category_name']
#     category_description = data['category_description']
#     category_image = data['category_image']

#     category = Category.objects.get(id=categoryId)
#     category.category_name = category_name
#     category.category_description = category_description
#     category.category_image = category_image

#     category.save()

#     return JsonResponse({'status': 'ok'})