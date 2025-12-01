from django.db import models
from patient.models import Patient
from food_type.models import FoodType
from django.db.models import Q

class FoodPreference(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    hates = models.BooleanField(default=False)
    loves = models.BooleanField(default=False)

    def __str__(self):
        if self.hates:
            return f"{self.user} hates {self.food_type}"
        if self.loves:
            return f"{self.user} loves {self.food_type}"
        return f"{self.user} has no preference for {self.food_type}"
        
class Meta:
    constraints = [
        models.UniqueConstraint(
                fields=['user', 'food_type'],
                name='unique_user_food_type_preference'
            ),
        models.CheckConstraint(
            check=~(Q(hates=True) & Q(loves=True)),
            name="not_both_true"
        )
    ]