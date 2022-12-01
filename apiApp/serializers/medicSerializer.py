from apiApp.models.medic import Medic
# from apiApp.models.user import User
# from apiApp.serializers.userSerializer import UserSerializer
from rest_framework import serializers
# from drf_writable_nested import WritableNestedModelSerializer

class MedicSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False, read_only=True) 
    class Meta:
        model = Medic
        fields = [ "id", "user", "professional_card", "speciality"]

        # def to_representation(self, obj):
        #     medic = Medic.objects.get(id=obj.id)
        #     user = User.objects.get(user = obj.id)
        #     return {
        #             "id": medic.id,
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
        #             "professional_card": medic.professional_card,
        #             "speciality": medic.speciality
        #         }    