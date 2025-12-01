from django.db import models
from logged_food.models import LoggedFood
from meal_type.models import MealType
from model_meal_type_component.models import ModelMealTypeComponent

class LoggedMeal(models.Model):
    food = models.ForeignKey(LoggedFood, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    model_meal_type_component = models.ForeignKey(ModelMealTypeComponent, on_delete=models.CASCADE, null=True, blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)