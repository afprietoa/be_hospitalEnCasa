from django.db import models
from .user import User

class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField( 'Relationship', default='',max_length=80)