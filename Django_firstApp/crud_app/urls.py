from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('list/', views.user_list, name='user_list'),
    path('update/<str:username>/', views.update_user, name='update_user'),
    path('delete/<str:username>/', views.delete_user, name='delete_user'),
]
