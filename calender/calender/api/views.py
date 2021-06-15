from rest_framework.response import Response
from book.models import Patient
from .serializers import PatientSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST',])
def create(request):
    serializer = PatientSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success" : True,
            "message" : "Booking successfull"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
            "success" : False,
            "message" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)