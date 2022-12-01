from rest_framework import generics, status
from rest_framework.response import Response

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.conf import settings
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.backends import TokenBackend

from apiApp.serializers.patientSerializer import PatientSerializer
from apiApp.serializers.userSerializer import UserSerializer
from apiApp.models.patient import Patient

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request):
        print("GET of all Medics")
        queryset = self.get_queryset()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST of Medic")
        userData = request.data.pop('user')
        serializerU  = UserSerializer(data=userData)
        serializerU.is_valid(raise_exception=True)
        user = serializerU.save()
        enfData = request.data 
        enfData.update({"user":user.id})
        serializerEnf = PatientSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)
        # tokenData = {
        #              "username":request.data["username"],
        #              "password":request.data["password"]
        #             }
        # tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        # tokenSerializer.is_valid(raise_exception=True)
        # return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) 

class PatientRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET of Medic")
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token, verify=False)
        # if(valid_data['user_id'] != kwargs['pk']):
        #     stringResponse ={'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT of Medic")
        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token, verify=False)
        # if(valid_data['user_id'] != kwargs['pk']):
        #     stringResponse ={'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)