from django.db import models
from user.models import User

class NutritionalGoal(models.Model):
    goal_choices = {
        -1: "lose",
        0: "maintain",
        1: "gain"
    }

    calorie_budget = models.IntegerField()
    protein_percentage = models.FloatField()
    carbs_percentage = models.FloatField()
    fat_percentage = models.FloatField()
    weight_goal = models.FloatField()
    goal = models.CharField(choices=goal_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # progress_speed = DERIVADA

    def __str__(self):
        return self.goal