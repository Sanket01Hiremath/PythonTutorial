from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

restaurants = {}
customers = {}
orders = []

@csrf_exempt
def register_restaurant(request):
    if request.method == 'POST':
        restaurant_name = request.POST.get('name')
        inventory = request.POST.get('inventory')
        restaurants[restaurant_name] = {'inventory': inventory}
        return JsonResponse({'message': 'Restaurant registered successfully.'})

@csrf_exempt
def manage_inventory(request, restaurant_name):
    if request.method == 'GET':
        if restaurant_name in restaurants:
            return JsonResponse(restaurants[restaurant_name]['inventory'], safe=False)
        else:
            return JsonResponse({'message': 'Restaurant not found.'}, status=404)

@csrf_exempt
def check_orders(request, restaurant_name):
    if request.method == 'GET':
        restaurant_orders = [order for order in orders if order['restaurant'] == restaurant_name]
        return JsonResponse(restaurant_orders, safe=False)

@csrf_exempt
def register_customer(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customers[customer_name] = {}
        return JsonResponse({'message': 'Customer registered successfully.'})

@csrf_exempt
def view_restaurants(request):
    if request.method == 'GET':
        return JsonResponse(list(restaurants.keys()), safe=False)

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer')
        restaurant_name = request.POST.get('restaurant')
        items = request.POST.get('items')
        orders.append({'customer': customer_name, 'restaurant': restaurant_name, 'items': items})
        return JsonResponse({'message': 'Order placed successfully.'})
