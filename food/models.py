from django.db import models
from food_type.models import FoodType

class Food(models.Model):
    description = models.CharField(max_length=100)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.description