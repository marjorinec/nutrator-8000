from django.db import models
from food_type.models import FoodType

class Patient(models.Model):
    biological_sex_choices = {
        "F": "female",
        "M": "male"
    }

    physical_activity_levels = {
        1.2: "sedentário (pouco ou nenhum exercício)", # 1.2
        1.375: "pouco ativo (exercício/esporte leve 1-3x/semana)", # 1.375
        1.55: "moderadamente ativo (exercício/esporte moderado 3-5x/semana)", # 1.55
        1.725: "muito ativo (exercício/esporte pesado 6-7x/semana)", # 1.725
        1.9: "extremamente ativo (exercício/esporte pesado e trabalho físico intenso diariamente ou treino de 2x/dia)" # 1.9
    }

    # TMB homens = 88.362 + (13.397 * peso [kg]) + (4.799 * altura [cm]) – (5.677 * idade) 
    # TMB mulheres = 447.593 + (9.247 * peso) + (3.098 * altura) – (4.330 * idade)

    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.FloatField()
    biological_sex = models.CharField(choices=biological_sex_choices)
    physical_activity_level = models.FloatField(choices=physical_activity_levels)
    food_type = models.ManyToManyField(FoodType, through="food_preference.FoodPreference")
    basal_metabolic_rate = models.FloatField(editable=False, null=True, blank=True)

    def __str__(self):
        return self.name