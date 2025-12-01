from django.contrib import admin
from .models import NutritionalGoal

@admin.register(NutritionalGoal)
class NutritionalGoalAdmin(admin.ModelAdmin):
    readonly_fields = ('progress_speed',)
    fields = (
        'calorie_budget',
        'carbs_percentage',
        'protein_percentage',
        'fat_percentage',
        'weight_goal',
        'goal',
        'user',
    )

    list_display = ( 'user', 'goal', 'weight_goal', 'calorie_budget', 'carbs_percentage', 'protein_percentage', 'fat_percentage',)
    list_filter = ('user', 'goal')