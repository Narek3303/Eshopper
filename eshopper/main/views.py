from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Carousel_Header
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, ReviewForm, SearchForm
from .models import Profile, Review
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .cart import Cart
from django.contrib.auth.models import User
from cart.forms import CartAddProductForm
from django.conf import settings
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.postgres.search import SearchVector


# def base_view(request):
#     cart = Cart(request)
#
#     return render(request, 'main/base.html', {'cart': cart})




class HomeListView(ListView):
    template_name = 'main/index.html'


    def get(self, request, slug=None):

        category = None
        categories = Category.objects.all()
        category_6 = Category.objects.all()[:6]
        products = Product.objects.filter(available=True)
        cart = Cart(request)

        just_arrived = products[:8]

        carousel_active = Carousel_Header.objects.first()
        carousel = Carousel_Header.objects.all()[1:5]


        if slug:
            category = get_object_or_404(Category,
                                         slug=slug)
            products = products.filter(category=category)


        return render(request, self.template_name, {'category': category,
                                                    'products': products,
                                                    'categories': categories,
                                                    'category_6': category_6,
                                                    'just_arrived': just_arrived,
                                                    'cart': cart,
                                                    'carousel_active':carousel_active,
                                                    'carousel':carousel})




    def post(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    reviews = Review.objects.filter(product=product.id)[:5]

    reviews_count = Review.objects.filter(status=True, product=product.id).count()




    return render(request,
                  'main/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'reviews': reviews,
                   'reviews_count': reviews_count,
                   })


# @login_required
# def course_details(request, course_slug):
#     user = request.user
#     review_product = Product.objects.get(slug=course_slug)
#     reviews_count = Review.objects.filter(status=True).count()
#     rating_count = sum(i for i in Review.objects.filter(rating='rating')) / Review.objects.filter(rating='rating').count()
#
#     return render(request, 'main/detail.html', {'user': user,
#                                                 'review_product': review_product,
#                                                 'reviews_count': reviews_count,
#                                                 'rating_count': rating_count})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('shop:products')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('shop:products')





def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return redirect('shop:login')
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})




def add_review(request, slug):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, slug=slug)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        content = form.cleaned_data['review']
        author = request.user
        review = Review()
        review.product = product
        review.user = author
        review.rating = rating
        review.review = content
        review.created_date = datetime.datetime.now()
        review.save()
        return redirect(url)

    return render(request, 'main/detail.html', {'form':form, 'product': product})





# def shop_search(request):
#     form = SearchForm()
#     query = None
#     results = []
#
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Product.objects.annotate(
#                 search=SearchVector('name', 'description'),
#             ).filter(search=query)
#
#
#     return render(request,
#                   'main/search.html',
#                   {'form': form,
#                    'query': query,
#                    'results': results})


