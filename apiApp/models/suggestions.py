from django.db import models
from .medic import Medic
from .clinicHistory import ClinicHistory

class Suggestions(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField( 'Description', default='',max_length=50)
    health_benefits = models.CharField( 'Benfits', default='',max_length=80)
    health_risks = models.CharField( 'Risks', default='',max_length=80)
    # medic = models.ForeignKey(Medic,on_delete=models.CASCADE)
    historic = models.ForeignKey(ClinicHistory, related_name='suggestions',on_delete=models.CASCADE)