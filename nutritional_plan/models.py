from django.db import models
from nutritional_goal.models import NutritionalGoal

class NutritionalPlan(models.Model):
    name = models.CharField(max_length=30)
    nutritional_goal = models.OneToOneField(
        NutritionalGoal,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    meal_type = models.ManyToManyField("meal_type.MealType", through="meal_type_nutritional_plan.MealTypeNutritionalPlan")

    def __str__(self):
        return self.name