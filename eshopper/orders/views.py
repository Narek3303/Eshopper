from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import HttpResponse
from django.urls import reverse



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                cart.clear()

                request.session['order_id'] = order.id

                return redirect(reverse('payment:process'))


    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/checkout.html',
                  {'cart': cart, 'form': form})