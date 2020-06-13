from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, "store/store.html", context)

def login_page(request):
    return render(request, "store/login.html")

def register_page(request):
    return render(request, "store/register.html")

def clothes(request):
    products = Product.objects.all().distinct('name')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    '''
    sizes = {}
    for i in range(len(products)):
        sizes[i] = []

    for product in products:
        prods = Product.objects.filter(name=product.name)
        for i in range(len(prods)):
            sizes[list(products).index(product)].append(prods[i].clothing_size)
    '''
    context = {
        'products': products,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, "store/clothes.html", context)

def clothes_detail(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    product = Product.objects.get(id=pk)
    products = Product.objects.filter(name=product.name)
    sizes = []
    for product in products:
        sizes.append(product.clothing_size)

    context = {
        'product': product,
        'sizes': sizes,
        'cartItems': cartItems
    }
    return render(request, "store/clothesdetail.html", context)

def shoes(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all().distinct('name')

    print(products)
    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, "store/shoes.html", context)

def shoes_detail(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    product = Product.objects.get(id=pk)
    products = Product.objects.filter(name=product.name)
    sizes = []
    for product in products:
        sizes.append(product.shoe_size)

    context = {
        'product': product,
        'sizes': sizes,
        'cartItems': cartItems
    }
    return render(request, "store/clothesdetail.html", context)

def accessories(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, "store/accessories.html", context)

def accessories_detail(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
        'cartItems': cartItems

    }
    return render(request, "store/accessoriesdetail.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, "store/cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, "store/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print("ProductId", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #print(order)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    #print(orderItem.quantity)
    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    
    orderItem.save()

    #print(orderItem.quantity)
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    print(transaction_id)
    data = json.loads(request.body)


    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            country = data['shipping']['country'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
            )

    else:
        print("User is not logged in!")

    return JsonResponse("Payment complete!", safe=False)