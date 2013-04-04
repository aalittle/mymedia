from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from media.models import Medium
from media.serializers import MediaSerializer

@api_view(['GET', 'POST'])
def medium_list(request, format=None):
    """
    List all mediums, or create a new medium.
    """
    if request.method == 'GET':
        media = Medium.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MediaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET', 'PUT', 'DELETE'])
def medium_detail(request, pk, format=None):
    """
    Retrieve, update or delete a medium instance.
    """              
    try:
        medium = Medium.objects.get(pk=pk)
    except Medium.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MediaSerializer(medium)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MediaSerializer(medium, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        medium.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)