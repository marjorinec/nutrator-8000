from django.contrib import admin

from .models import MealType

@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'allows_snack',
        'contains_rich_in_carb',
        'contains_rich_in_prot',
        'contains_rich_in_fat',
        'contains_rich_in_fiber',
        'is_dessert',
    )

    list_display = ('name', 'allows_snack', 'contains_rich_in_carb', 'contains_rich_in_prot', 'contains_rich_in_prot', 'contains_rich_in_fat', 'contains_rich_in_fiber', 'is_dessert')
    list_filter = ('name',)