from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant

# restaurants = {}
# inventory={}
# orders={}
order = {}
integer = 0
restaurant_id = 0
is_button_disabled = False


@csrf_exempt
def login(request):
    return render(request, 'login.html')


@csrf_exempt
def register(request):
    return render(request, 'newRestaurant.html')


@csrf_exempt
def register_restaurant(request):
    previous_page = request.META.get('HTTP_REFERER')

    restaurant_name = request.POST.get('name')
    description = request.POST.get("desc")
    # without db
    # restaurant={}
    # restaurant['name']=restaurant_name
    # inventory[restaurant_id]={}
    # restaurant['inventory']=inventory[restaurant_id]
    # global integer
    # restaurants[integer] = restaurant
    # integer+=1

    # with db
    restaurant = Restaurant(name=restaurant_name,
                            desc=description, inventory={}, order={})
    restaurant.save()
    return redirect(previous_page)


@csrf_exempt
def view_restaurants(request, num):
    restaurants = Restaurant.objects.all()
    
    global is_button_disabled
    if num == 1:
        is_button_disabled = False
        return render(request, 'home.html', {'restaurants': restaurants})
    else:
        print(num)
        is_button_disabled = True
        return render(request, 'home.html', {'restaurants': restaurants, 'btn_dis': is_button_disabled})


@csrf_exempt
def restaurant_view(request, key):
    restaurant = get_object_or_404(Restaurant, pk=key)
    global restaurant_id
    restaurant_id = key
    print(restaurant.inventory)
    return render(request, 'restaurant.html', {'restaurant': restaurant, 'btn_dis': is_button_disabled})


@csrf_exempt
def order_summary(request):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    orders = restaurant.order
    global order, integer
    if len(order) != 0:
        orders[integer] = order
        order = {}
        integer += 1
    else:
        print('add some thing into bag to proceed')
    restaurant.save()
    return render(request, 'orders.html', {'orders': orders})


@csrf_exempt
def all_orders(request):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    orders = restaurant.order
    print(orders)
    return render(request, 'orders.html', {'orders': orders})


def add_to_order(request, key):
    # restaurant = restaurants[restaurant_id]
    # inv=restaurant['inventory']
    # price=inv[sub_key]
    # if sub_key in order:
    #     order[sub_key]=[price,order[sub_key][1]+1]
    # else:
    #     order[sub_key]=[price,1]
    # print(order)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    inv = restaurant.inventory
    price = inv[key]
    if key in order:
        order[key] = [price, order[key][1]+1]
    else:
        order[key] = [price, 1]
    print(order)
    return render(request, 'restaurant.html', {'restaurant': restaurant, 'btn_dis': is_button_disabled})


@csrf_exempt
def view_inventory(request):
    return render(request, 'inventory.html')


@csrf_exempt
def manage_inventory(request):
    previous_page = request.META.get('HTTP_REFERER')
    key = request.POST.get('key')
    value = request.POST.get('value')
    # restaurant=restaurants[restaurant_id]
    # inv=restaurant['inventory']
    # inv[key]=value
    # print(inventory[restaurant_id])
    print(restaurant_id)
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    inv = restaurant.inventory
    print(inv)
    inv[key] = value
    print(inv)
    restaurant.save()
    return redirect(previous_page)


def register_user(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    username=request.POST.get('username')
    password=request.POST.get('password')

    