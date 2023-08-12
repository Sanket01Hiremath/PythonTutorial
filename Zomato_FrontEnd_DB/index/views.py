from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

restaurants = {}
inventory={}
orders={}
order={}
integer=0
restaurant_id=0

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
    restaurant={}
    restaurant['name']=restaurant_name
    inventory[restaurant_id]={}
    restaurant['inventory']=inventory[restaurant_id]
    global integer
    restaurants[integer] = restaurant
    integer+=1
    return redirect(previous_page)

@csrf_exempt
def view_restaurants(request,num):
    if num==1:
        return render(request, 'home.html', {'json_data': restaurants})
    else:
        print(num)
        is_button_disabled=True
        return render(request, 'home.html', {'json_data': restaurants,'btn_dis':is_button_disabled})
        
@csrf_exempt
def restaurant_view(request,key):
    restaurant = restaurants[int(key)]
    global restaurant_id
    restaurant_id=int(key)
    return render(request, 'restaurant.html', {'restaurant': restaurant})


@csrf_exempt
def order_summary(request):
    global integer
    global order

    if len(order)!=0:
        orders[integer]=order
        order={}
        integer+=1
    else:
        print('add some thing inmto bag to proceed')
    print(order)
    print(orders)
    return render(request, 'orders.html', {'orders': orders[integer-1]})

@csrf_exempt
def all_orders(request):
    return render(request, 'orders.html', {'orders': orders})

def add_order(request,sub_key):
    restaurant = restaurants[restaurant_id]
    inv=restaurant['inventory']
    price=inv[sub_key]
    if sub_key in order:
        order[sub_key]=[price,order[sub_key][1]+1]
    else:
        order[sub_key]=[price,1]
    print(order)
    return render(request, 'restaurant.html', {'restaurant': restaurant})

@csrf_exempt
def view_inventory(request):
    return render(request, 'inventory.html')

@csrf_exempt
def manage_inventory(request):
    previous_page = request.META.get('HTTP_REFERER')
    key=request.POST.get('key')
    value=request.POST.get('value')
    restaurant=restaurants[restaurant_id]
    inv=restaurant['inventory']
    inv[key]=value
    print(inventory[restaurant_id])
    return redirect(previous_page)
