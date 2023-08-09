from django.urls import path
from . import views

urlpatterns = [
    path('register/restaurant/', views.register_restaurant, name='register_restaurant'),
    path('restaurant/<str:restaurant_name>/inventory/', views.manage_inventory, name='manage_inventory'),
    path('restaurant/<str:restaurant_name>/orders/', views.check_orders, name='check_orders'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('view/restaurants/', views.view_restaurants, name='view_restaurants'),
    path('place/order/', views.place_order, name='place_order'),
]

