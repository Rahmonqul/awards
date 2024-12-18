from rest_framework.serializers import ModelSerializer
from .models import *


class AwardSerializer(ModelSerializer):
    class Meta:
        model=Award
        fields=['id', 'name', 'bio','image', 'count']
