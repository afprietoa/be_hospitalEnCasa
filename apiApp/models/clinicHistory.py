from datetime import datetime
from django.db import models
from .patient import Patient
from .medic import Medic
from .nurse import Nurse

class ClinicHistory(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField( 'Date-Time', default=datetime.now,max_length=50)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic,on_delete=models.CASCADE)
    diagnostic = models.CharField( 'Diagnostic', default='',max_length=50)
    description = models.CharField( 'Description', default='',max_length=50)
    # nuse = models.ForeignKey(Nurse,on_delete=models.CASCADE)