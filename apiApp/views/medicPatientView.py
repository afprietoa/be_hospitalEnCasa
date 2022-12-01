from rest_framework import status
from rest_framework.response import Response
from apiApp.models.medicPatient import MedicPatient
from apiApp.serializers.medicPatientSerializer import MedicPatientSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def createMedicPatient(request):
    if request.method == 'GET':
        model = MedicPatient.objects.all()
        serializer = MedicPatientSerializer(model, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MedicPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','DELETE'])
def detailMedicPatient(request, pk):
    if request.method == 'PUT':
        model = MedicPatient.objects.get(pk=pk)
        serializer = MedicPatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model = MedicPatient.objects.get(pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)