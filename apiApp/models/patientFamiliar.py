from django.db import models
from .patient import Patient
from .familiar import Familiar

class PatientFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    familiar = models.ForeignKey(Familiar,on_delete=models.CASCADE)