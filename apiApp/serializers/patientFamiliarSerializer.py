from apiApp.models.patientFamiliar import PatientFamiliar
from rest_framework import serializers

class PatientFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientFamiliar
        fields = ["id", "patient", "familiar" ]