from django.db import models
from food_type.models import FoodType
from meal_type_nutritional_plan.models import MealTypeNutritionalPlan

class ModelMealTypeComponent(models.Model):
    food_type_id = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    weight = models.FloatField()
    meal_type_nutritional_plan = models.ForeignKey(MealTypeNutritionalPlan, on_delete=models.CASCADE)
    meal_calorie_budget = models.FloatField(null=True, blank=True, editable=False) #TODO definir o cálculo

    def __str__(self):
        return f"{self.meal_type_nutritional_plan}"