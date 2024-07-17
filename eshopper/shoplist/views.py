
from main.models import Product
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST






def shop_listview(request):

    products = Product.objects.filter(available=True)

    return render(request, 'shoplist/shop.html', {'products':products})

