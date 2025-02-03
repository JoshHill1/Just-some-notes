from django.urls import path
from .views import hello_world, Statistics, PublicSpeaking, Business, Psychology

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('statistics/', Statistics, name='Statistics'),
    path('public-speaking/', PublicSpeaking, name='Public Speaking'),
    path('business/', Business, name='Business'),
    path('psychology/', Psychology, name='Psychology'),
]
