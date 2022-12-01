from rest_framework import status
from rest_framework.response import Response
from apiApp.models.patientFamiliar import PatientFamiliar
from apiApp.serializers.patientFamiliarSerializer import PatientFamiliarSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def createPatientFamiliar(request):
    if request.method == 'GET':
        model = PatientFamiliar.objects.all()
        serializer = PatientFamiliarSerializer(model, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientFamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','DELETE'])
def detailPatientFamiliar(request, pk):
    if request.method == 'PUT':
        model = PatientFamiliar.objects.get(pk=pk)
        serializer = PatientFamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model = PatientFamiliar.objects.get(pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)