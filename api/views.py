from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Award
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator
from rest_framework import filters
from .filters import AwardOrderFilter, AwardOrderFilterYear
from django_filters.rest_framework import DjangoFilterBackend
class AwardApiView(APIView):
    def get(self, request):
        awards = Award.objects.all()
        paginator = Paginator(awards, 6)

        page_number = request.query_params.get('page', 1)
        page_obj = paginator.get_page(page_number)

        serializer = AwardDetailSerializer(page_obj.object_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UsersApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PresidentDecreeApiView(ListAPIView):
    queryset = PresidentDecree.objects.all()
    serializer_class = PresidenDecreeSerializer

class PresidentDecreeYearApiView(APIView):
    def get(self, request):

        years = (
            PresidentDecree.objects
            .values_list('year', flat=True)
            .distinct()
        )
        unique_years = sorted({year.year for year in years})
        return Response(unique_years)

class AwardOrderApiView(APIView):
    def get(self, request):
        award_order = AwardOrder.objects.all()
        serializer = AwardOrderSerializer(award_order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AwardOwnerSearchApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AwardOwnerSerializer
    # permission_classes = []  #

    filter_backends = (filters.SearchFilter,)
    search_fields = ['fio']

class AwardOwnerFilterApiView(ListAPIView):
    queryset = AwardOrder.objects.all()
    serializer_class = AwardOwnerFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AwardOrderFilter

class AwardFilterYearApiview(ListAPIView):
    queryset = AwardOrder.objects.all()
    serializer_class = AwardOownerFilterYearSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AwardOrderFilterYear