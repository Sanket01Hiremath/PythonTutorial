from django.urls import path
from . import views

app_name = 'greetings'
urlpatterns = [
    path('/', views.welcome),
    path('greet/<str:name>/', views.greet),
    path('farewell/<str:name>/', views.farewell),
]
