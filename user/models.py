from django.db import models
from food_type.models import FoodType

class User(models.Model):
    biological_sex_choices = {
        "F": "female",
        "M": "male"
    }

    physical_activity_levels = {
        1: "sedentário",
        2: "atividade leve",
        3: "atividade moderada",
        4: "atividade intensa"
    }

    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.FloatField()
    biological_sex = models.CharField(choices=biological_sex_choices)
    physical_activity_level = models.CharField(choices=physical_activity_levels)
    food_preferences = models.ManyToManyField(FoodType, through="FoodPreference")
    # basal_metabolic_rate = derivado


    def __str__(self):
        return self.name
    
class FoodPreference(models.Model):
    feelings_choices = {
        "loves": "loves",
        "hates": "hates"
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    feeling = models.CharField(choices=feelings_choices)

    def __str__(self):
        return self.feeling
