
import random
import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderProduct
from carts.models import Cart, CartItem
from carts.views import cartIDs
from shop.models import Product

@login_required(login_url="login")
def place_order(request, total=0, quantity=0, cart_item=None, carts=0):
    current_user = request.user
    final = 0
    tax = 0
    try:
        cart = Cart.objects.get(cart_id=cartIDs(request))
        cart_item = CartItem.objects.filter(cart=cart, is_active=True)
        
        if request.user.is_authenticated:
            cart_item = cart_item.filter(user=request.user)
            
        for item in cart_item:
            carts += item.quantity
            total += (item.product.price * item.quantity)
        tax = 2 * total / 100
        final = total + tax
    except Cart.DoesNotExist:
        pass

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line1 = form.cleaned_data['address_line1']
            data.address_line2 = form.cleaned_data['address_line2']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = final
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            
            order_number = random.randint(100000, 999999)
            data.order_number = order_number
            data.save()

            return redirect('payment', order_number=order_number)
    else:
        form = OrderForm()

    context = {
        "total": total,
        "quantity": quantity,
        "cart_item": cart_item,
        "final": final,
        "tax": tax,
        "carts": carts,
        'form': form,
    }
    return render(request, "place-order.html", context)

@login_required(login_url="login")
def payment(request, order_number):
    order = Order.objects.get(order_number=order_number)
    total = 0
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)

    for item in cart_items:
        order_product = OrderProduct()
        order_product.order = order
        order_product.user = request.user
        order_product.product = item.product
        order_product.quantity = item.quantity
        order_product.price = item.product.price
        order_product.is_ordered = True
        order_product.save()
        
        for variation in item.variations.all():
            order_product.variation.add(variation)
        
        total += (item.product.price * item.quantity)

    tax = 2 * total / 100
    final = total + tax
    context = {
        'order': order,
        'total': total,
        'final': final,
        'cart_items':cart_items
    }
    
    return render(request, 'payment.html', context)

def dashboard(request):
    pass
