from django.contrib import admin

from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    readonly_fields = (
        'kcal_display',
        'total_carbs_display',
        'protein_display',
        'total_fat_display',
    )

    fields = (
        'weight',
        'food_type',
        'kcal_display',
        'total_carbs_display',
        'protein_display',
        'total_fat_display',
    )

    def kcal_display(self, obj):
        if not obj or obj.kcal is None:
            return "—"
        return f"{obj.kcal:.2f}"
    kcal_display.short_description = "kcal"

    def total_carbs_display(self, obj):
        if not obj or obj.total_carbs is None:
            return "—"
        return f"{obj.total_carbs:.2f} g"
    total_carbs_display.short_description = "Carboidratos"

    def protein_display(self, obj):
        if not obj or obj.protein is None:
            return "—"
        return f"{obj.protein:.2f} g"
    protein_display.short_description = "Proteína"

    def total_fat_display(self, obj):
        if not obj or obj.total_fat is None:
            return "—"
        return f"{obj.total_fat:.2f} g"
    total_fat_display.short_description = "Gordura"

    list_display = ('food_name', 'weight', 'kcal', 'total_carbs', 'protein', 'total_fat')
    list_filter = ('food_name', 'weight', 'kcal', 'total_carbs', 'protein', 'total_fat')

    