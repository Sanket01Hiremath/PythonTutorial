from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant,User,Order,Conversation
from django.contrib import messages
from django.http import JsonResponse
import openai

order = {}
restaurant_id = 0
is_button_disabled = False
user_id=0

@csrf_exempt
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def register_user(request):
    previous_page = request.META.get('HTTP_REFERER')
    name=request.POST.get("name")
    age=request.POST.get("age")
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=User(name=name,age=age,username=username,password=password,type='C',wallet=0)
    user.save()
    return redirect(request, previous_page)

@csrf_exempt
def view_restaurants(request):
    previous_page = request.META.get('HTTP_REFERER')
    username=request.POST.get("username")
    password=request.POST.get("password")
    restaurants = Restaurant.objects.all()
    user = User.objects.get(username=username)

    global is_button_disabled,user_id

    if  user.type=='C' and user.password==password:
        user_id=user.pk
        is_button_disabled = True
        return render(request, 'home.html', {'restaurants': restaurants, 'btn_dis': is_button_disabled, 'user':user})
    else:
        messages.error(request, f"User '{username}' not found/password not match!.")
        return redirect(previous_page,{'user_not_found': True})

@csrf_exempt
def add_res(request):
    return render(request, 'newRestaurant.html')

@csrf_exempt
def reg_new_res(request):
    previous_page = request.META.get('HTTP_REFERER')
    restaurant_name = request.POST.get('name')
    description = request.POST.get("desc")
    restaurant = Restaurant(name=restaurant_name,desc=description, inventory={})
    restaurant.save()
    return redirect(previous_page)

@csrf_exempt
def restaurant_view(request, key):
    restaurant = get_object_or_404(Restaurant, pk=key)
    global restaurant_id
    restaurant_id = key
    return render(request, 'restaurant.html', {'restaurant': restaurant, 'btn_dis': is_button_disabled})

@csrf_exempt
def inventory_link(request):
    return render(request, 'inventory.html')

@csrf_exempt
def manage_inventory(request):
    previous_page = request.META.get('HTTP_REFERER')
    key = request.POST.get('key')
    value = request.POST.get('value')
    print(restaurant_id)
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    inv = restaurant.inventory
    print(inv)
    inv[key] = value
    print(inv)
    restaurant.save()
    return redirect(previous_page)

@csrf_exempt
def order_summary(request):
    previous_page = request.META.get('HTTP_REFERER')
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    user = User.objects.get(pk=user_id)
    
    global order

    if len(order) != 0:
        o=Order(restaurant=restaurant,user=user,order=order)
        o.save()
        temp_det=o
        order = {}
        return render(request, 'orders.html', {'orders': temp_det})
    else:
        print('add some thing into bag to proceed')
        return redirect(previous_page)

@csrf_exempt
def all_orders(request):
    previous_page = request.META.get('HTTP_REFERER')
    orders = Order.objects.all(restaurant=restaurant_id,user=user_id)
    if len(orders) != 0:
        return render(request, 'orders.html', {'orders': orders})
    else:
        print('Empty!')
        return redirect(previous_page)

@csrf_exempt
def add_to_order(request, key):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    inv = restaurant.inventory
    price = inv[key]
    if key in order:
        order[key] = [price, order[key][1]+1]
    else:
        order[key] = [price, 1]
    print(order)
    return render(request, 'restaurant.html', {'restaurant': restaurant, 'btn_dis': is_button_disabled})


openai.api_key = "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"

@csrf_exempt
def chatbot_view(request):
    previous_page=request.META.get('HTTP_REFERER')
    if request.method == "POST":
        user_message = request.POST.get("user_message")
        conversation_history = request.POST.get("conversation_history", "")

        conversation_prompt = f"User: {user_message}\nChatbot:{conversation_history}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Or any other engine you prefer
            prompt=conversation_prompt,
            max_tokens=50
        )

        chatbot_response = response.choices[0].text.strip()

        # Save the conversation to the database if needed
        Conversation.objects.create(
            user_message=user_message,
            chatbot_response=chatbot_response
        )

        return JsonResponse({"chatbot_response": chatbot_response})

    return redirect(previous_page)