from datetime import date
from django.db import models
from .user import User

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField( 'Birth_Date', default=date.today, max_length=50)
    address = models.CharField( 'Address', default='', max_length=50)
    city = models.CharField( 'City', default='', max_length=50)
    longitude = models.CharField( 'Longitude', default='', max_length=50)
    latitude = models.CharField( 'Latitude', default='', max_length=50)