from django.contrib import admin

from .models import ModelMealTypeComponent

@admin.register(ModelMealTypeComponent)
class ModelMealTypeComponentAdmin(admin.ModelAdmin):
    readonly_fields = ('meal_calorie_budget',)
    fields = ('food_type_id', 'weight', 'meal_type_nutritional_plan')
    list_display = ('food_type_id', 'weight', 'meal_type_nutritional_plan', 'meal_calorie_budget')
    list_filter = ('meal_type_nutritional_plan',)



#     User.objects.find(id=12)

#     # Q: me retorne um modelo de refeição dentro de um plano alimentar
#     ModelMealTypeComponent.objects.filter(meal_type__name="almoço", nutritional_plan_id=12)
#     [
#         {
#             food_type:12
#             weight:12
#         },
#     ]


# class ModeloDeRefeicao:
#     def find(nutritional_plan, meal_type):
        