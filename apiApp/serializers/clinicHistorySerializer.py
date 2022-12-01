from apiApp.models.clinicHistory import ClinicHistory
from rest_framework import serializers

from apiApp.serializers.vitalSignsSerializer import VitalSignsSerializer
from apiApp.models.vitalSigns import VitalSigns

from apiApp.serializers.suggestionsSerializer import SuggestionsSerializer
from apiApp.models.suggestions import Suggestions

from drf_writable_nested import WritableNestedModelSerializer
from setuptools.config._validate_pyproject.fastjsonschema_validations import validate

class ClinicHistorySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    vital_signs = VitalSignsSerializer(many = True)
    suggestions = SuggestionsSerializer(many = True)

    class Meta:
        model = ClinicHistory
        fields = [ "id", "date_time", "patient", "medic", "diagnostic", "description", "vital_signs", "suggestions" ]

    def create(self, validated_data):
        vitalSignsData = validated_data.pop('vital_signs')
        suggestionsData = validated_data.pop('suggestions')
        historic = ClinicHistory.objects.create(**validated_data)

        for vitalSign in vitalSignsData:
            VitalSigns.objects.create(historic=historic, **vitalSign)

        for suggestion in suggestionsData:
            Suggestions.objects.create(historic=historic, **suggestion)
        
        return historic

    def to_representation(self, obj):
        historic = ClinicHistory.objects.get(id=obj.id)
        vital_signs = VitalSigns.objects.get(historic = obj.id)
        suggestions = Suggestions.objects.get(historic = obj.id)
        return {
            "id": historic.id,
            "date_time": historic.date_time,
            "patient": historic.patient,
            "medic": historic.medic,
            "diagnostic": historic.diagnostic,
            "description": historic.description,
            "vital_signs" :{
                "id": vital_signs.id,
                "date_time": vital_signs.date_time,
                "oximetry": vital_signs.oximetry,
                "glycemia": vital_signs.glycemia,
                "blood_pressure": vital_signs.blood_pressure,
                "temperature": vital_signs.temperature,
                "heart_rate":vital_signs.heart_rate,
                "respiratory_rate": vital_signs.respiratory_rate
            },
            "suggestions" :{
                "id": suggestions.id,
                "health_benefits": suggestions.health_benefits,
                "health_risks": suggestions.health_risks,
                "description": suggestions.description,
            }
        }