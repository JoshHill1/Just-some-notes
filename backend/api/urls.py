from django.urls import path
from .views import StatisticsList

urlpatterns = [
    path('statistics/', StatisticsList.as_view(), name='statistics-list'),
]
