from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import Users


# @api_view(['GET'])
# def dataUsers(request):
#     usersList = Users.objects.all()

#     data = []
#     for user in usersList:
#         userData = {
#             'id': user.id,
#             'firstname': user.firstname,
#             'lastname': user.lastname,
#             'country': user.country
#         }
#         data.append(userData)

#     return JsonResponse({'data': data})


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
