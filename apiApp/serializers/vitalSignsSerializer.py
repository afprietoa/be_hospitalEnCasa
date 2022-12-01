from apiApp.models.vitalSigns import VitalSigns
from rest_framework import serializers

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = [ "id", "date_time", "oximetry", "glycemia", "blood_pressure", "temperature", "heart_rate", "respiratory_rate" ]