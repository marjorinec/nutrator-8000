from django.contrib import admin
from .models import NutritionalPlan

@admin.register(NutritionalPlan)
class NutritionalPlanAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'nutritional_goal',
    )

    list_display = ('name', 'nutritional_goal')
    list_filter = ('name', 'nutritional_goal')
