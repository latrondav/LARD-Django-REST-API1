from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manufacturer
from .serializers import ManufacturerSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def GetAllManufacturers(request):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def PostManufacturers(request):
    if request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'message': 'Manufacturer Added Successfully'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def DeleteManufacturer(request, id):
    try:
        manufacturer = Manufacturer.objects.get(pk=id)
    except Manufacturer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        manufacturer.delete()
        return Response({'message': 'Manufacturer Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)


