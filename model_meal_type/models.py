from django.db import models
from food.models import Food
from meal_type.models import MealType
from nutritional_plan.models import NutritionalPlan

class ModelMealType(models.Model):
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    nutritional_plan = models.ForeignKey(NutritionalPlan, on_delete=models.CASCADE)
    # meal_calorie_budget DERIVADO