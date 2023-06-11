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










#Category

# @api_view(['PUT'])
# def updateCategory(request):
#     data = json.loads(request.body)
#     categoryId = data['id']
#     category_name= data['category_name']
#     category_description = data['category_description']
#     price = data['price']

#     Categories = Categorys.objects.get(id=categoryId)
#     Categories.category_name = category_name
#     Categories.category_description = category_description
#     Categories.price = price
#     Categories.save()

#     return JsonResponse({'status': 'ok'})