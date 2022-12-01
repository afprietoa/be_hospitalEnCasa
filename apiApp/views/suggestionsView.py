# from rest_framework import status
# from rest_framework.response import Response
# from apiApp.models.suggestions import Suggestions
# from apiApp.serializers.suggestionsSerializer import SuggestionsSerializer
# from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def createSuggestions(request):
#     if request.method == 'GET':
#         model = Suggestions.objects.all()
#         serializer = SuggestionsSerializer(model, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SuggestionsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['PUT','DELETE'])
# def detailSuggestions(request, pk):
#     if request.method == 'PUT':
#         model = Suggestions.objects.get(pk=pk)
#         serializer = SuggestionsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         model = Suggestions.objects.get(pk=pk)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)