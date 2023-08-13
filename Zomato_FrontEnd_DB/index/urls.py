from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/<int:num>', views.view_restaurants, name='view_restaurants'),
    path('register/restaurant/', views.register_restaurant, name='register_restaurant'),
    path('register/', views.register, name='register_restaurant'),
    path('view_restaurant/<str:key>', views.restaurant_view, name='restaurant_view'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('orders/', views.all_orders, name='all_orders'),
    path('add_to_order/<str:key>', views.add_to_order, name='add_to_order'),
    path('inventory/', views.view_inventory, name='view_inventory'),
    path('inventory/manage_inventory/', views.manage_inventory, name='manage_inventory'),
]
