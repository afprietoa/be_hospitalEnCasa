from apiApp.models.medicPatient import MedicPatient
from rest_framework import serializers

class MedicPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicPatient
        fields = ["id", "medic","patient" ]