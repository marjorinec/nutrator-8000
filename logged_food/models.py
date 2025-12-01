from django.db import models
from food_type.models import FoodType

class LoggedFood(models.Model):
    weight = models.IntegerField()
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    kcal = models.FloatField(null=True, blank=True, editable=False)
    total_carbs = models.FloatField(null=True, blank=True, editable=False)
    protein = models.FloatField(null=True, blank=True, editable=False)
    total_fat = models.FloatField(null=True, blank=True, editable=False)
    food_name = models.CharField(null=True, blank=True, editable=False)
    logged_at = models.DateTimeField(auto_now_add=True)

    def get_kcal(self):
        return round(self.weight * self.food_type.kcal_per_un, 1)
    
    def get_total_carbs(self):
        return round(self.weight * self.food_type.total_carbs_per_un, 1)
    
    def get_protein(self):
        return round(self.weight * self.food_type.protein_per_un, 1)
    
    def get_total_fat(self):
        return round(self.weight * self.food_type.total_fat_per_un, 1)

    def get_food_name(self):
        return f"{self.food_type.description} - {self.food_type.brand_name}"

    def __str__(self):
        return f"{self.get_food_name()}"
    
    def save(self, *args, **kwargs):
        self.kcal = self.get_kcal()
        self.total_carbs = self.get_total_carbs()
        self.protein = self.get_protein()
        self.total_fat = self.get_total_fat()
        self.food_name = self.get_food_name()

        super().save(*args, **kwargs)