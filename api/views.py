from rest_framework.response import Response
from rest_framework import status
from .serializers import AwardSerializer
from .models import Award
from rest_framework.views import APIView

class AwardApiView(APIView):
    def get(self, request):
        awards = Award.objects.all()  # Retrieve all awards from the database
        serializer = AwardSerializer(awards, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)
