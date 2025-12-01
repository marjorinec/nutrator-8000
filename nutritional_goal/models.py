from django.db import models
from patient.models import Patient

class NutritionalGoal(models.Model):
    goal_choices = {
        "lose": "lose",
        "maintain": "maintain",
        "gain": "gain"
    }

    calorie_budget = models.IntegerField()
    protein_percentage = models.FloatField()
    carbs_percentage = models.FloatField()
    fat_percentage = models.FloatField()
    weight_goal = models.FloatField()
    goal = models.CharField(choices=goal_choices)
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    progress_speed = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.goal