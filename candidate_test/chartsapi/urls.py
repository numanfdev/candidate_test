from django.urls import path
from .views import ChartDataAPI

urlpatterns = [
    path('/', ChartDataAPI.as_view(), name='chart-data-api'),
]
