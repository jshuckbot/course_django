from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Имя {self.first_name} дата регистрации: {self.created}"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Товар: {self.name} количество: {self.total} дата поступления: {self.created}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Номер заказа: {self.pk} дата составления: {self.created}"
