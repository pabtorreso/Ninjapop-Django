from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='CartItem')

    def get_total_quantity(self):
        total_quantity = 0
        for item in self.cartitem_set.all():
            total_quantity += item.quantity
        return total_quantity

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, default=0)

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=0)
    imagen1 = models.ImageField(upload_to='', default='default_image.png')
    imagen2 = models.ImageField(upload_to='', default='default_image.png')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
