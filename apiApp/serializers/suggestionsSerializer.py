from apiApp.models.suggestions import Suggestions
from rest_framework import serializers

class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = [ "id", "description","health_benefits", "health_risks"]