from django.db import models
from .patient import Patient
from .medic import Medic

class MedicPatient(models.Model):
    id = models.AutoField(primary_key=True)
    medic = models.ForeignKey(Medic,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)