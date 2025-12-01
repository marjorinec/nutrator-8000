from django.contrib import admin

from .models import LoggedMeal

@admin.register(LoggedMeal)
class LoggedMealAdmin(admin.ModelAdmin):
    readonly_fields = (
        'logged_at',
    )

    fields = (
        'food',
        'meal_type',
        'model_meal_type_component',
    )

    list_display = ('food', 'meal_type', 'model_meal_type_component', 'logged_at')
    list_filter = ('food', 'meal_type', 'model_meal_type_component', 'logged_at')