# from rest_framework import status
# from rest_framework.response import Response
# from apiApp.models.vitalSigns import VitalSigns
# from apiApp.serializers.vitalSignsSerializer import VitalSignsSerializer
# from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def createVitalSigns(request):
#     if request.method == 'GET':
#         model = VitalSigns.objects.all()
#         serializer = VitalSignsSerializer(model, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = VitalSignsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['PUT','DELETE'])
# def detailVitalSigns(request, pk):
#     if request.method == 'PUT':
#         model = VitalSigns.objects.get(pk=pk)
#         serializer = VitalSignsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         model = VitalSigns.objects.get(pk=pk)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)