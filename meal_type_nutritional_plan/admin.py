from django.contrib import admin
from .models import MealTypeNutritionalPlan

@admin.register(MealTypeNutritionalPlan)
class MealTypeNutritionalPlanAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'nutritional_plan')