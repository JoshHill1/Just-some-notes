# from django.urls import path
# from .views import hello_world, Statistics, PublicSpeaking, Business, Psychology

# urlpatterns = [
#     path('hello/', hello_world, name='hello_world'),
#     path('statistics/', Statistics, name='Statistics'),
#     path('public-speaking/', PublicSpeaking, name='Public Speaking'),
#     path('business/', Business, name='Business'),
#     path('psychology/', Psychology, name='Psychology'),
# ]


# backend/api/urls.py
from django.urls import path
from .views import page1, page2, page3, page4

urlpatterns = [
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('page4/', page4, name='page4'),
]
