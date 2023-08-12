from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/restaurant/', views.register_restaurant, name='register_restaurant'),
    path('login/<int:num>', views.view_restaurants, name='view_restaurants'),
    path('register/', views.register, name='register_restaurant'),
    path('view_restaurant/<str:key>', views.restaurant_view, name='restaurant_view'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('orders/', views.all_orders, name='all_orders'),
    path('add_order/<str:sub_key>', views.add_order, name='add_order'),
    path('inventory/', views.view_inventory, name='view_inventory'),
    path('inventory/manage_inventory/', views.manage_inventory, name='manage_inventory'),
]
