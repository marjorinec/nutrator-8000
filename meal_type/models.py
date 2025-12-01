from django.db import models

class MealType(models.Model):
    name = models.CharField(max_length=200)
    allows_snack = models.BooleanField(default=False)
    contains_rich_in_carb = models.BooleanField()
    contains_rich_in_prot = models.BooleanField()
    contains_rich_in_fat = models.BooleanField()
    contains_rich_in_fiber = models.BooleanField()
    is_dessert = models.BooleanField(default=False)
    nutritional_plan = models.ManyToManyField("nutritional_plan.NutritionalPlan", through="meal_type_nutritional_plan.MealTypeNutritionalPlan")

    def __str__(self):
        return self.name