from django.db import models

class MealType(models.Model):
    name = models.CharField
    allows_snack = models.BooleanField()
    contains_prot_source = models.BooleanField()
    contains_carb_source = models.BooleanField()
    contains_fat_source = models.BooleanField()
    contains_fiber_source = models.BooleanField()
    is_dessert = models.BooleanField()