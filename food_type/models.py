from django.db import models
from django.db.models.functions import Lower


class FoodType(models.Model):
    MEASURE_UNIT_CHOICES = (
        ("g", "gram"),
        ("mL", "milliliter"),
    )

    def __str__(self):
        return self.description
    
    def get_nutri_info_per_un(self, nutri_info, units):
        multiplier = units / self.portion_size

        return nutri_info * multiplier

    def get_all_nutri_info_values_per_un(self, units):
        nutri_values_per_units = {
            'kcal': self.get_nutri_info_per_un(self.kcal, units),
            'carb': self.get_nutri_info_per_un(self.total_carbs, units),
            'prot': self.get_nutri_info_per_un(self.protein, units),
            'fat': self.get_nutri_info_per_un(self.total_fat, units)
        }

        return nutri_values_per_units
    
    def get_rich_in(self):
        nutri_values_per_100_un = self.get_all_nutri_info_values_per_un(100)
        rich_percentage = 0.2

        macros_percentage_values = [
            {
                'macro': 'carb',
                'percentage': nutri_values_per_100_un['carb'] / 100,
                'rich': nutri_values_per_100_un['carb'] / 100 > rich_percentage
            },
            {
                'macro': 'prot',
                'percentage': nutri_values_per_100_un['prot'] / 100,
                'rich': nutri_values_per_100_un['prot'] / 100 > rich_percentage
            },
            {
                'macro': 'fat',
                'percentage': nutri_values_per_100_un['fat'] / 100,
                'rich': nutri_values_per_100_un['fat'] / 100 > rich_percentage
            },
        ]

        macros_percentage_values = [
            macro for macro in macros_percentage_values
            if macro["percentage"] >= rich_percentage
        ]

        ordered_macros = sorted(macros_percentage_values, key=lambda x: x["percentage"], reverse=True)

        return ordered_macros

    def save(self, *args, **kwargs):
        self.kcal_per_un = self.get_nutri_info_per_un(self.kcal, 1)
        self.total_carbs_per_un = self.get_nutri_info_per_un(self.total_carbs, 1)
        self.total_fat_per_un = self.get_nutri_info_per_un(self.total_fat, 1)
        self.protein_per_un = self.get_nutri_info_per_un(self.protein, 1)
        self.rich_in = self.get_rich_in()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} — {self.brand_name}"

    description = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    portion_size = models.IntegerField()
    measure_unit = models.CharField(choices=MEASURE_UNIT_CHOICES)
    snack = models.BooleanField(default=False)
    kcal = models.IntegerField()
    total_carbs = models.FloatField()
    protein = models.FloatField()
    total_fat = models.FloatField()
    container_total_weight = models.IntegerField(null=True, blank=True)

    kcal_per_un = models.FloatField(null=True, blank=True, editable=False)
    total_carbs_per_un = models.FloatField(null=True, blank=True, editable=False)
    total_fat_per_un = models.FloatField(null=True, blank=True, editable=False)
    protein_per_un = models.FloatField(null=True, blank=True, editable=False)
    rich_in = models.JSONField(null=True, blank=True, editable=False)

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

class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['description', 'brand_name', 'container_total_weight'],
                name='unique_desc_brand_weight'
            )
        ]

        