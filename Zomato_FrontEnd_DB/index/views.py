from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant,User,Order
from django.contrib import messages


order = {}
restaurant_id = 0
is_button_disabled = False
user_id=0

@csrf_exempt
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def logout(request):
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
    return redirect(previous_page)

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
        return render(request, 'home.html', {'restaurants': restaurants, 'btn_dis': is_button_disabled})
    elif user.type=='A':
        user_id=user.pk
        is_button_disabled = False
        return render(request, 'home.html', {'restaurants': restaurants, 'btn_dis': is_button_disabled})
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
        order = {}
        return render(request, 'orders.html', {'orders': o.order})
    else:
        print('add some thing into bag to proceed')
        return redirect(previous_page)

@csrf_exempt
def all_orders(request):
    previous_page = request.META.get('HTTP_REFERER')
    orders = Order.objects.all()
    print(orders)
    for o in orders:
        print(o.order)
    if len(orders) != 0:
        return render(request, 'orders.html', {'orders': orders})
    else:
        print('Empty!')
        return redirect(previous_page)

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

def cart(request):
    global order

    if len(order) != 0:
        print(order)
        return render(request, 'cart.html', {'orders': order, 'value': False})
    else:
        print('add some thing into bag to proceed')
        return render(request, 'cart.html', {'value': True})
    
def payment(request):
    return render(request, 'payments.html')
