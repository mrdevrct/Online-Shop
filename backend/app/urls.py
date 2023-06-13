from django.urls import path
from . import views

urlpatterns = [
    # # # User
    # path('add/user', views.addUser , name='add'),
    # path('data/users', views.dataUsers , name='users'),
    # path('delete/user', views.deleteUser , name='delete'),
    # path('update/user', views.updateUser , name='update'),
    
    # # # Product
    # path('add/product', views.addProduct , name='add_product'),
    # path('data/product', views.dataProduct , name='products'),
    # path('delete/product', views.deleteProduct , name='delete_products'),
    # path('update/product', views.updateProduct , name='update_products'),

    # # # Category
    # path('add/category', views.addCategory , name='add_category'),
    # path('data/category', views.dataCategory , name='categories'),
    # path('delete/category', views.deleteCategory , name='delete_categories'),
    # path('update/category', views.updateCategory , name='update_categories'),


    # # # Cart
    path('add/cart', views.addCart , name='add_cart'),
    path('data/cart', views.dataCart , name='carts'),
    path('delete/cart', views.deleteCart , name='delete_cart'),
    path('update/cart', views.updateCart , name='update_cart'),


    # # # Order
    path('add/order', views.addOrder , name='add_order'),
    path('data/order', views.dataOrder , name='orders'),
    path('delete/order', views.deleteOrder , name='delete_order'),
    path('update/order', views.updateOrder , name='update_order'),

    # # # orderDetails
    path('add/orderDetails', views.addOrderDetails , name='add_orderDetails'),
    path('data/orderDetails', views.dataOrderDetails , name='orderDetails'),
    path('delete/orderDetails', views.deleteOrderDetails , name='delete_orderDetails'),
    path('update/orderDetails', views.updateOrderDetails , name='update_orderDetails')
]