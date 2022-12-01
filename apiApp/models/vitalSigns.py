from datetime import datetime
from django.db import models
from .patient import Patient
from .clinicHistory import ClinicHistory

class VitalSigns(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField( 'Date_Time', default=datetime.now ,max_length=50)
    oximetry = models.CharField( 'Oximetry', default='',max_length=50)
    glycemia = models.CharField( 'Glycemia', default='',max_length=50)
    blood_pressure = models.CharField( 'Blood_Pressure, default=''',max_length=50)
    temperature = models.CharField( 'Temperature', default='',max_length=50)
    heart_rate = models.CharField( 'Heart_Rate', default='',max_length=50)
    respiratory_rate = models.CharField( 'Respiratory_Rate', default='',max_length=50)
    historic = models.ForeignKey(ClinicHistory, related_name='vital_signs',on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient,on_delete=models.CASCADE)