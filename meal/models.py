from django.db import models
from food.models import Food
from meal_type.models import MealType
from model_meal_type.models import ModelMealType

class Meal(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    model_meal_type = models.ForeignKey(ModelMealType, on_delete=models.CASCADE)