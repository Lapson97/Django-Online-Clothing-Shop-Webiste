from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

'''
class ShoeSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)

class ClothingSize(models.Model):
    size = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.size
'''

class Product(models.Model):
    CATEGORY = (
        ('Clothing', 'Clothing'),
        ('Shoes', 'Shoes'),
        ('Accessories', 'Accessories')
    )

    SHOE_SIZE = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    )

    CLOTHING_SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )

    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    name = models.CharField(max_length=200, null=True)
    shoe_size = models.CharField(max_length=200, null=True, choices=SHOE_SIZE, blank=True)
    clothing_size = models.CharField(max_length=200, null=True, choices=CLOTHING_SIZE, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        if self.clothing_size:
            return self.name + " " + self.clothing_size
        elif self.shoe_size:
            return self.name + " " + self.shoe_size
        else:
            return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.get_total
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.quantity
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address