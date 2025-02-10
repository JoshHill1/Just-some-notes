# from django.urls import path
# from .views import statistics, public_speaking, business, psychology

# urlpatterns = [
#     path('statistics/', statistics, name='statistics'),
#     path('public-speaking/', public_speaking, name='public-speaking'),
#     path('business/', business, name='business'),
#     path('psychology/', psychology, name='psychology'),
# ]

# urls.py
from django.urls import path
from .views import StatisticsList

urlpatterns = [
    path('statistics/', StatisticsList.as_view(), name='statistics-list'),
]
