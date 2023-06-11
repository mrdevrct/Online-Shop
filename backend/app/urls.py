from django.urls import path
from . import views

urlpatterns = [
    path('add/user', views.addUser , name='add'),
    # path('data/users', views.dataUsers , name='users'),
    # path('delete/user', views.deleteUser , name='delete'),
    # path('update/user', views.updateUser , name='update'),
]