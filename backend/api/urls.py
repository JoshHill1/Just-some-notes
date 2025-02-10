from django.urls import path
from .views import statistics, public_speaking, business, psychology

urlpatterns = [
    path('statistics/', statistics, name='statistics'),
    path('public-speaking/', public_speaking, name='public-speaking'),
    path('business/', business, name='business'),
    path('psychology/', psychology, name='psychology'),
]
