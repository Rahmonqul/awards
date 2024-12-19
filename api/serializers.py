from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class AwardDetailSerializer(ModelSerializer):
    class Meta:
        model=Award
        fields=['id', 'name', 'bio','image', 'count']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class PresidenDecreeSerializer(ModelSerializer):
    class Meta:
        model=PresidentDecree
        fields='__all__'

class PresidenDecreeYearSerializer(ModelSerializer):
    class Meta:
        model=PresidentDecree
        fields=['year']


class AwardOrderSerializer(ModelSerializer):
    # Вложенные сериализаторы для вычисляемых полей
    award_name = SerializerMethodField()
    award_image = SerializerMethodField()
    user_fio = SerializerMethodField()
    user_image = SerializerMethodField()
    user_position=SerializerMethodField()


    class Meta:
        model = AwardOrder
        fields = ['award_name', 'award_image', 'user_fio', 'user_image', 'user_position']

    def get_award_name(self, obj):
        return obj.award.name


    def get_award_image(self, obj):
        return obj.award.image.url if obj.award.image else None

    def get_user_fio(self, obj):
        return obj.user.fio
    def get_user_position(self, obj):
        return obj.user.position

    def get_user_image(self, obj):
        return obj.user.image.url if obj.user.image else None


class AwardSerializer(ModelSerializer):
    class Meta:
        model = Award
        fields = ['name', 'image']

class AwardOwnerSerializer(ModelSerializer):
    # Сериализация наград пользователя
    awards = SerializerMethodField()

    class Meta:
        model = User
        fields = ['fio', 'position', 'image', 'awards']  # Добавляем поле 'awards' для наград

    # Метод для получения всех наград пользователя
    def get_awards(self, obj):
        # Получаем все связанные награды для этого пользователя
        award_orders = AwardOrder.objects.filter(user=obj)
        awards = [award_order.award for award_order in award_orders]
        return AwardSerializer(awards, many=True).data

class AwardOwnerFilterSerializer(ModelSerializer):
    fio = SerializerMethodField()
    owner_image = SerializerMethodField()
    awards = SerializerMethodField()

    class Meta:
        model = AwardOrder
        fields = ['fio', 'owner_image', 'awards']

    def get_fio(self, obj):
        return obj.user.fio

    def get_owner_image(self, obj):
        return obj.user.image.url if obj.user.image else None

    def get_awards(self, obj):
        return {
            "name": obj.award.name,
            "image": obj.award.image.url if obj.award.image else None,
            "date_awarded": obj.number_president_decree.year.strftime('%Y-%m-%d'),
        }

class AwardOownerFilterYearSerializer(ModelSerializer):
    user = SerializerMethodField()
    award = SerializerMethodField()
    decree_details = SerializerMethodField()

    class Meta:
        model = AwardOrder
        fields = ['user', 'award', 'decree_details']

    def get_user(self, obj):

        return {
            "fio": obj.user.fio,
            "image": obj.user.image.url if obj.user.image else None,
        }

    def get_award(self, obj):

        return {
            "name": obj.award.name,
            "image": obj.award.image.url if obj.award.image else None,
        }

    def get_decree_details(self, obj):

        return {
            "number_president_decree": obj.number_president_decree.number_president_decree,
            "awards_given": AwardOrder.objects.filter(
                number_president_decree=obj.number_president_decree
            ).count(),
        }