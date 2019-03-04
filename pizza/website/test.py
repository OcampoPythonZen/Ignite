
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import topping
from .models import Topping, Pizza, Order

# Create your tests here.
# Por falta de tiempo solo se testea el menu de Ingredientes que
# es el menu que almacena "Toppings", puedes agregar ingredientes y verlos en la siquiente
# ventana de Pizzas, donde se despliegan los Ingredientes creados.

#################
# Testing urls #
################
class TestUrls(SimpleTestCase):

    def test_topping_url_resolved(self):
        url = reverse('topping')
        self.assertEquals(resolve(url).func, topping)

##################
# Testing views #
#################
class TestViews(TestCase):

    def test_views_topping_resolved(self):
        client = Client()
        response = client.get(reverse('topping'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/topping_form.html')
        
###################
# Testing models #
#################
class TestModels(TestCase):

    def setup(self):
        Topping.objects.create(
            topping_name = 'my_new_topping_name',
            calories = 33.33,
            unit = 'cal',
            price = 22.22
        )
    
    # def test_topping_model_resolved(self):
    #     topping_name = Topping.topping_name.get(topping_name='topping_name')
    #     self.assertEqual(topping_name,topping_name)