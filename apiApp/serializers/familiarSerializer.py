from apiApp.models.familiar import Familiar
# from apiApp.models.user import User
# from apiApp.serializers.userSerializer import UserSerializer
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Familiar
        fields = [ "id", "user", "relationship" ]

        # def to_representation(self, obj):
        #     familiar = Familiar.objects.get(id=obj.id)
        #     user = User.objects.get(user = obj.id)
        #     return {
        #             "id": familiar.id,
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
        #             "relationship": familiar.relationship
        #         }    