from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_link'),
    path('logout', views.login, name='logout_link'),
    path('register_user', views.register_user, name='register_user'),
    path('login', views.view_restaurants, name='view_restaurants'),
    path('view_restaurant/<str:key>', views.restaurant_view, name='restaurant_view'),
    path('add_res', views.add_res, name='add_restaurant'),
    path('reg_new_res', views.reg_new_res, name='register_new_restaurant'),
    path('inventory', views.inventory_link, name='inventory_link'),
    path('manage_inventory', views.manage_inventory, name='manage_inventory'),
    path('order_summary', views.order_summary, name='order_summary'),
    path('orders', views.all_orders, name='all_orders'),
    path('add_to_order/<str:key>', views.add_to_order, name='add_to_order'),
    path("chatbot/", views.chatbot_view, name="chatbot_view"),
]