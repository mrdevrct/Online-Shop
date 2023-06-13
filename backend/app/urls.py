from django.urls import path
from . import views

urlpatterns = [
    # User
    path('add/user', views.addUser , name='add'),
    # path('data/users', views.dataUsers , name='users'),
    # path('delete/user', views.deleteUser , name='delete'),
    # path('update/user', views.updateUser , name='update'),
    
    # # Product
    # path('add/product', views.addProduct , name='add_product'),
    # path('data/users', views.dataProduct , name='products'),
    # path('delete/user', views.deleteProduct , name='delete_products'),
    # path('update/user', views.updateProduct , name='update_products'),

    # # # Category
    # path('add/category', views.addCategory , name='add_category'),
    # path('data/category', views.dataCategory , name='categories'),
    # path('delete/category', views.deleteCategory , name='delete_categories'),
    # path('update/category', views.updateCategory , name='update_categories')



]