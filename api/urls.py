from django.urls import  path
from .views import AwardApiView

urlpatterns=[
    path("awards/", AwardApiView.as_view(), name="apihome")
]