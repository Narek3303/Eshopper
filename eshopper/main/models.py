from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='media', null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def get_absolute_url(self):
        return reverse('shop:product_slug',
                       args=[self.slug])



class Image(models.Model):
    img = models.ImageField(upload_to='media')


    def __str__(self):
        return 'Image'



class ModelColor(models.Model):
    color = models.CharField(max_length=15)


    def __str__(self):
        return self.color

class ModelSize(models.Model):
    size = models.CharField(max_length=3)


    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField('Name', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    image = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    description = models.TextField(null=True)
    product_description = models.TextField(null=True)
    information = models.TextField(null=True)
    color = models.ManyToManyField(ModelColor, related_name='color_color')
    size = models.ManyToManyField(ModelSize, related_name='size_size')


    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name





    class Meta:
        indexes = [models.Index(fields=['-created'])]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])




class Carousel_Header(models.Model):
    title1 = models.CharField(max_length=70)
    title2 = models.CharField(max_length=70)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.title2




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


    def __str__(self):
        return f'Profile of {self.user.username}'









class Review(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
    rating = models.FloatField()
    review = models.TextField(max_length=500, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user} to {self.product.name}'




    def total_rating(self):
        return sum(i for i in self.rating)


    class Meta:

        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]







