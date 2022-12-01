from apiApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "id", "rol", "doc_type", "doc_number", "first_name", "last_name", "e_mail", "cellphone", "genre", "username", "password" ]