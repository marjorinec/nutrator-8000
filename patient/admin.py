from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    readonly_field = ('basal_metabolic_rate',)

    fields = (
        'name',
        'height',
        'weight',
        'biological_sex',
        'physical_activity_level',
    )

    list_display = ('name', 'height', 'weight', 'biological_sex', 'physical_activity_level', 'basal_metabolic_rate',)
    list_filter = ('name', 'biological_sex', 'physical_activity_level',)