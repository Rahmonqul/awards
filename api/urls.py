from django.urls import  path
from .views import AwardApiView, UsersApiView, PresidentDecreeApiView, PresidentDecreeYearApiView, AwardOrderApiView, AwardOwnerSearchApiView

urlpatterns=[
    path("awards/", AwardApiView.as_view(), name="apiawards"),
    path("users/", UsersApiView.as_view(), name="apiusers"),
    path("users/search/", AwardOwnerSearchApiView.as_view(), name="apiuserssearch"),
    path("decree/", PresidentDecreeApiView.as_view(), name="apidecree"),
    path("decree/year/", PresidentDecreeYearApiView.as_view(), name="apidecreeyear"),
    path("order/", AwardOrderApiView.as_view(), name="apiorder"),
]