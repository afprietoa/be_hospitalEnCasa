from ast import Delete
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from apiApp.models.clinicHistory import ClinicHistory
from apiApp.serializers.clinicHistorySerializer import ClinicHistorySerializer

class ClinicHistoryCreateView(views.APIView):

    # def post(self, request):
    #     serializar=ClinicHistorySerializer(data=request.data)
    #     if serializar.is_valid():
    #         serializar.save()
    #         return Response(serializar.data,status=status.HTTP_201_CREATED)
    #     return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, *args, **kwargs):
        serializer = ClinicHistorySerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class ClinicHistoryRetrieveUpdateDestroyView(views.APIView):

    def get(self, request, pk, format=None):
        model=ClinicHistory.objects.get(pk=pk)
        serializer=ClinicHistorySerializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model=ClinicHistory.objects.get(pk=pk)
        serializer=ClinicHistorySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo=ClinicHistory.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#  from rest_framework import status
# from rest_framework.response import Response
# from apiApp.models.clinicHistory import ClinicHistory
# from apiApp.serializers.clinicHistorySerializer import ClinicHistorySerializer
# from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def createClinicHistory(request):
#     if request.method == 'GET':
#         model = ClinicHistory.objects.all()
#         serializer = ClinicHistorySerializer(model, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ClinicHistorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['PUT','DELETE'])
# def detailClinicHistory(request, pk):
#     if request.method == 'PUT':
#         model = ClinicHistory.objects.get(pk=pk)
#         serializer = ClinicHistorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         model = ClinicHistory.objects.get(pk=pk)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)