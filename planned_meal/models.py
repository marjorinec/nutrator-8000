from django.db import models
from nutritional_plan.models import NutritionalPlan
from food_type.models import FoodType

class PlannedMeal(models.Model):
    nutritional_plan = models.ForeignKey(NutritionalPlan, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    weight = models.IntegerField()
