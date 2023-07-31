from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contact(models.Model):
    mail=models.EmailField()
    msg=models.CharField(max_length=550)
class Category(models.Model):
    title=models.CharField(max_length=50,verbose_name="category title")
    slug=models.SlugField(max_length=55,verbose_name="category slug")
    category_image=models.ImageField(upload_to="category",blank=True,null=True,verbose_name="category image")
    is_active=models.BooleanField(verbose_name="Is active")

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=150,verbose_name="product title")
    slug=models.SlugField(max_length=150,verbose_name="product slug")
    product_image=models.ImageField(upload_to="product",blank='True',null="True",verbose_name="product image")
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.ForeignKey(Category,verbose_name="product category",on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="is_active")
    is_featured=models.BooleanField(verbose_name="is_featured")
    productStock=models.PositiveIntegerField()

class Relatedimage(models.Model):
    products=models.ForeignKey(Product,default=None,on_delete=models.CASCADE)
    image=models.FileField(upload_to='relimg',null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,verbose_name='Product',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default='1',verbose_name='quantity')

    def __str__(self):
        return str(self.user)
    @property
    def total_price(self):
        return self.quantity*self.product.price





