from django.db import models
from food_type.models import FoodType
from nutritional_plan.models import NutritionalPlan
from planned_meal.models import PlannedMeal

class PlannedFood(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    nutritional_plan = models.ForeignKey(NutritionalPlan, on_delete=models.CASCADE)
    planned_meal = models.ForeignKey(PlannedMeal, on_delete=models.CASCADE)

class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['nutritional_plan', 'planned_meal'],
            name='unique_nutri_plan_planned_meal'
        )
    ]

