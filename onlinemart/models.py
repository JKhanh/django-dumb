from django.db import models


# Create your models here.
class Fullname(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Account(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Address(models.Model):
    street = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Customer(models.Model):
    name = models.ForeignKey(Fullname, on_delete=models.SET_NULL).null = True
    account = models.ForeignKey(Account, on_delete=models.SET_NULL).null = True
    address = models.ForeignKey(Address, on_delete=models.SET_NULL).null = True
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    base_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=999999, default="This is a product")


class Cart(models.Model):
    total = models.FloatField(default=0)


class Item(models.Model):
    name = models.CharField(max_length=200)
    amount_remain = models.IntegerField(default=0)
    price_sale = models.FloatField(default=0)
    shop_name = models.CharField(max_length=200)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    destination = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField()
    total = models.FloatField(default=0)


class Payment(models.Model):
    type = models.CharField(max_length=200)
    total = models.FloatField(default=0)


class Shipment(models.Model):
    type = models.CharField(max_length=200)
    cost = models.FloatField(default=15000)
