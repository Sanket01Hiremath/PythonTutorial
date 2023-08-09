from django.shortcuts import render
from django.http import JsonResponse

restaurants = {}
customers = {}
orders = []

def register_restaurant(request):
    if request.method == 'POST':
        restaurant_name = request.POST.get('name')
        inventory = request.POST.get('inventory')
        restaurants[restaurant_name] = {'inventory': inventory}
        return JsonResponse({'message': 'Restaurant registered successfully.'})

def manage_inventory(request, restaurant_name):
    if request.method == 'GET':
        if restaurant_name in restaurants:
            return JsonResponse(restaurants[restaurant_name]['inventory'], safe=False)
        else:
            return JsonResponse({'message': 'Restaurant not found.'}, status=404)

def check_orders(request, restaurant_name):
    if request.method == 'GET':
        restaurant_orders = [order for order in orders if order['restaurant'] == restaurant_name]
        return JsonResponse(restaurant_orders, safe=False)

def register_customer(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customers[customer_name] = {}
        return JsonResponse({'message': 'Customer registered successfully.'})

def view_restaurants(request):
    if request.method == 'GET':
        return JsonResponse(list(restaurants.keys()), safe=False)

def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer')
        restaurant_name = request.POST.get('restaurant')
        items = request.POST.get('items')
        orders.append({'customer': customer_name, 'restaurant': restaurant_name, 'items': items})
        return JsonResponse({'message': 'Order placed successfully.'})
