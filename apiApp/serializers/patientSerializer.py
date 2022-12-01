from apiApp.models.patient import Patient
# from apiApp.models.user import User
# from apiApp.serializers.userSerializer import UserSerializer
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Patient
        fields = [ "id", "user", "birth_date", "address", "city", "longitude", "latitude"]

        # def to_representation(self, obj):
        #     patient = Patient.objects.get(id=obj.id)
        #     user = User.objects.get(user = obj.id)
        #     return {
        #             "id": patient.id,
        #             "user":{
        #                 "id": user.id,
        #                 "rol": user.rol,
        #                 "doc_type": user.doc_type,
        #                 "doc_number": user.doc_number,
        #                 "first_name": user.first_name,
        #                 "last_name": user.last_name,
        #                 "e_mail": user.e_mail,
        #                 "cellphone": user.cellphone,
        #                 "genre": user.genre,
        #                 "username": user.username,
        #                 "password": user.password
                        
        #             },
        #             "birth_date": patient.birth_date, 
        #             "address": patient.address, 
        #             "city": patient.city, 
        #             "longitude": patient.longitude,
        #             "latitude": patient.latitude 
        #         }    