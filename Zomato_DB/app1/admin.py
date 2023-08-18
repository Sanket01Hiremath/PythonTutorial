from django.contrib import admin
from .models import Restaurant,User,Order,Conversation

admin.site.register(Restaurant)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Conversation)
