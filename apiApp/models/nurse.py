from django.db import models
from .user import User

class Nurse(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professional_card = models.BigIntegerField(default=0, unique=True)
    speciality = models.CharField( 'Speciality', default='', max_length=50)