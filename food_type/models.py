from django.db import models


class FoodType(models.Model):
    measure_unit_choices = {
        "g": "gram",
        "mL": "mililiter"
    }

    description = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    portion_size = models.IntegerField()
    measure_unit = models.CharField(choices=measure_unit_choices)
    snack = models.BooleanField()
    calories = models.IntegerField()
    total_carbs = models.FloatField()
    proteins = models.FloatField()
    total_fat = models.FloatField()
    container_total_weight = models.IntegerField()
    # total_carbs_per_un = models.FloatField() DERIVADO
    # total_fat_per_un = models.FloatField() DERIVADO
    # protein_per_un = models.FloatField() DERIVADO

    saturated_fat = models.FloatField(blank=True, null=True)
    polyunsaturated_fat = models.FloatField(blank=True, null=True)
    monounsaturated_fat = models.FloatField(blank=True, null=True)
    trans_fat = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    fiber = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    added_sugar = models.FloatField(blank=True, null=True)
    vitamin_a = models.FloatField(blank=True, null=True)
    vitamin_c = models.FloatField(blank=True, null=True)
    vitamin_d = models.FloatField(blank=True, null=True)
    iron = models.FloatField(blank=True, null=True)
    calcium = models.FloatField(blank=True, null=True)
    # source_of = models.CharField(choices=macro_choices) DERIVADO

    def __str__(self):
        return self.description