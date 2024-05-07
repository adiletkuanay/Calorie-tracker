from django.test import TestCase, Client

# Create your tests here.
from django.contrib.auth.models import User
from .models import Food, Consume
from django.urls import reverse

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

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()  
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_home_view_requires_login(self):
        response = self.client.get(reverse("home")) 
        self.assertEqual(response.status_code, 302)  
        self.assertIn("/login/", response.url) 

    def test_home_view_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "home.html")  