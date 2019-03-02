from django.db import models
from django.urls import reverse
from decimal import Decimal
import decimal

#Format to use with decimal numbers
quantity = Decimal('0.01')

# Create your models here.
class Customer(models.Model):
    """Create a customer profile to order pizza.
    """
    customer_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=90)
    
    def __str__(self):
        return f'Cliente {self.customer_name}'
        
    def get_absolute_url(self):
        return reverse("eocampo")

class Size(models.Model):
    """Pizza sizes to know the price.
    """
    size_name = models.CharField(max_length=30)
    price_size = models.DecimalField(default=0.00,decimal_places=2,max_digits=4)

    def __str__(self):
        return f'Tamaño {self.size_name}'

class Topping(models.Model):
    """Ingredient or topping into a pizza.
    """
    UNIT_USED = (
        ('cal','cal'),
        ('kcal','kcal'),
    )
    topping_name = models.CharField(max_length=30)
    calories = models.FloatField(default=0.00)
    unit = models.CharField('Unidades',max_length=5,choices=UNIT_USED,default=0.00)
    price_topping = models.DecimalField(default=1.00,decimal_places=2,max_digits=4)

    
    def __str__(self):
        return f'Ingrediente {self.topping_name}'

class Pizza(models.Model):
    """Pizza name to show customer
    """
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    price_pizza = models.DecimalField(default=0.00,decimal_places=2,max_digits=4)
    order_by = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    def save(self,*args,**kwargs):
        if not Pizza.objects.filter(id=self.id):
            super().save(*args,**kwargs)
        else:
            price = Decimal('0.00')
            if self.size:
                price = self.size.price_size
                print(price)
                for topping in toppings.all():
                    if topping.price_topping:
                        price =+ topping.price_topping
            self.price_pizza = decimal.Decimal(str(price)).quantize(quantity)
            print(price)
            super().save(*args,**kwargs)

    def __str__(self):
        if self.size.size_name:
            name = 'Pizza de tamaño ' + self.size.size_name
        else:
            name = 'Pizza'
        for topping in self.toppings.all():
            if topping.topping_name:
                name = name + ', ' + topping.topping_name
        return name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False, null = True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    subtotal = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    is_finished = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not Order.objects.filter(id=self.id):
            super().save(*args,**kwargs)
        else:
            decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
            self.subtotal = Decimal('0.00')
            for pizza in self.pizzas.all():
                self.subtotal += pizza.price_pizza
                for topping in self.pizza.toppings.all():
                    self.subtotal += topping.price_topping
            if self.subtotal < 30.00:
                self.total = self.subtotal + 8.00
            self.total = self.total.quantize(quantity)
            super().save(*args,**kwargs)

    def __str__(self):
        return f'ID: {self.id}'

    def get_absolute_url(self):
        return reverse("nuevo_cliente",kwargs={'pk':self.id})