from django.db import models
from meal_type.models import MealType
from nutritional_goal.models import NutritionalGoal

class NutritionalPlan(models.Model):
    name = models.CharField(max_length=30)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    nutritional_goal = models.OneToOneField(
        NutritionalGoal,
        on_delete=models.CASCADE,
        primary_key=True,
    )