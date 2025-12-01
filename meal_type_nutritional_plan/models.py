from django.db import models
from meal_type.models import MealType
from food_type.models import FoodType
from nutritional_plan.models import NutritionalPlan

class MealTypeNutritionalPlan(models.Model):
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    nutritional_plan = models.ForeignKey(
        NutritionalPlan,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Plano {self.nutritional_plan} - {self.meal_type}"