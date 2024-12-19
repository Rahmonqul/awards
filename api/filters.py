from django_filters import rest_framework as filters
from .models import AwardOrder

class AwardOrderFilter(filters.FilterSet):
    number_president_decree = filters.NumberFilter(field_name="number_president_decree__number_president_decree")
    year = filters.DateFilter(field_name="number_president_decree__year__year")
    order_type = filters.CharFilter(field_name="order_type", lookup_expr="exact")

    class Meta:
        model = AwardOrder
        fields = ['number_president_decree', 'year', 'order_type']

class AwardOrderFilterYear(filters.FilterSet):
    year = filters.NumberFilter(
        field_name="number_president_decree__year__year",  # Извлекаем год из даты
        lookup_expr="exact"
    )

    class Meta:
        model = AwardOrder
        fields = ['year']  # Фильтрация только по году