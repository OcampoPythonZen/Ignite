from django.db import models

# Create your models here.
class Calorie(models.Model):
    """Model to define the calories per ingredient, relationship 1:1 with Ingredent
    """
    UNITS_USED = (
        ('cal','cal'),
        ('kcal','kcal')
    )

    created_at = models.DateTimeField(auto_now = False, auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False, null = True)
    calories = models.FloatField(max_length=4)
    unity = models.CharField('Unidad de medida:', max_length=5, choices=UNITS_USED)


    def __str__(self):
        return f'Calories{self.calories} {self.unity}'

class Ingredient(models.Model):
    """Model to define the ingredents per pizza, relationship M:1 with pizza
    """
    calorie = models.OneToOneField(Calorie,on_delete=models.CASCADE,pimary_key=True) #Relationship 1:1 with Calorie
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False, null = True)
    is_active = models.BooleanField(default = True)
    ingredient_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'Ingredent{self.ingredient_name}'

class Pizza(models.Model):
    """Model to define the name of every pizza to show. relationship 1:M with ingredients
    """
    ingredients = models.ForeignKey(Ingredient,models.CASCADE)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False, null = True)
    is_active = models.BooleanField(default = True)
    pizza_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'Pizza name:{self.pizza_name}'

