from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Food, Consume

class FoodModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(name="Apple", carbs=25, protein=0.5, fats=0.2, calories=95)

    def test_food_str(self):
        self.assertEqual(str(self.food), "Apple")  
    def test_food_attributes(self):
        self.assertEqual(self.food.carbs, 25)
        self.assertEqual(self.food.protein, 0.5)
        self.assertEqual(self.food.fats, 0.2)
        self.assertEqual(self.food.calories, 95)
