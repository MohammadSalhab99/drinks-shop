from django.test import TestCase
from .models import Drink

# Testing the model
class DrinksTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testdrink = Drink.objects.create(name = "test_drink", description="Testing drink")
        testdrink.save()


    def test_drinks_model(self):
        drink = Drink.objects.get(id=1)
        actual_name = drink.name
        self.assertEqual(actual_name, "test_drink")