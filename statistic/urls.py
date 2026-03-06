from rest_framework.urls import *
from .views import *

urlpatterns = [
    path("statistic/", ShowStatistic.as_view(), name="statistics"),
]