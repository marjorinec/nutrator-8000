from django.contrib import admin
from .models import FoodType
from food_type.models import FoodType

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'kcal_per_un_display',
        'carbs_per_un_display',
        'protein_per_un_display',
        'fat_per_un_display',
        'rich_in_display',
    )

    fields = (
        'description',
        'brand_name',
        'portion_size',
        'measure_unit',
        # 'snack',
        'kcal',
        'total_carbs',
        'protein',
        'total_fat',
        # 'container_total_weight',
        'kcal_per_un_display',
        'carbs_per_un_display',
        'protein_per_un_display',
        'fat_per_un_display',
        'rich_in_display',
    )
    
    def kcal_per_un_display(self, obj):
        if not obj or obj.kcal_per_un is None:
            return "—"
        return f"{obj.kcal_per_un:.2f} kcal"
    kcal_per_un_display.short_description = f"kcal a cada unidade de medida"
    
    def carbs_per_un_display(self, obj):
        if not obj or obj.total_carbs_per_un is None:
            return "—"
        return f"{obj.total_carbs_per_un:.2f} g"
    carbs_per_un_display.short_description = f"Carboidratos a cada unidade de medida"

    def protein_per_un_display(self, obj):
        if not obj or obj.protein_per_un is None:
            return "—"
        return f"{obj.protein_per_un:.2f} g"
    protein_per_un_display.short_description = f"Proteína a cada unidade de medida"

    def fat_per_un_display(self, obj):
        if not obj or obj.total_fat_per_un is None:
            return "—"
        return f"{obj.total_fat_per_un:.2f} g"
    fat_per_un_display.short_description = f"Gordura a cada unidade de medida"

    def rich_in_display(self, obj):
        if not obj or not obj.rich_in:
            return "—"

        parts = []
        for item in obj.rich_in:
            macro = item["macro"]
            percent = item["percentage"] * 100
            parts.append(f"{macro} ({percent:.2f}%)")

        return ", ".join(parts)

    rich_in_display.short_description = "Rico em"

    list_display = ('description', 'brand_name', 'portion_size', 'measure_unit')
    # list_filter = ('description', 'brand_name', 'portion_size', 'measure_unit')
    list_filter = ('description', 'brand_name', 'portion_size', 'measure_unit', 'kcal', 'total_carbs', 'protein', 'total_fat')