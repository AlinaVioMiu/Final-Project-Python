from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=79)  # varchar
    icon = models.ImageField(upload_to='static/categories/', null=True,
                             blank=True)  # varchar + fisier in folderul statis

    def products(self):
        return Product.objects.filter(category=self)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=79)  # varchar
    description = models.TextField()  # text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # decimal
    stock = models.IntegerField()  # int
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)  # int + foreign key + stergi categoria, stergi si produsele
    image = models.ImageField(upload_to='static/products')  # varchar + fisier in folderul statis

    def __str__(self):
        return f'{self.stock} x {self.name} @ {self.price} lei'


class Client(AbstractUser):
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=255)

class Cart(models.Model):
    CART_STATUSES = (
        ('open', 'Deschis'),
        ('closed', 'Inchis')
    )
    status = models.CharField(max_length=30, choices=CART_STATUSES)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.status}'

    def cart_items(self):
        return CartItem.objects.filter(cart=self)

    def total(self):
        items = self.cart_items()
        totals = [i.total() for i in items]
        return sum(totals)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} {self.product.name} in {self.cart}'

    def total(self):
        return self.quantity * self.product.price




class ContactRequest(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    content = models.TextField()