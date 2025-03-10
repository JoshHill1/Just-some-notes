from django.urls import path
from .views import StatisticsList, PublicSpeakingList, BusinessList, PsychologyList, TestCommitList

urlpatterns = [
    path('statistics/', StatisticsList.as_view(), name='statistics-list'),
    path('public-speaking/', PublicSpeakingList.as_view(), name='public-speaking-list'),
    path('business/', BusinessList.as_view(), name='business-list'),
    path('psychology/', PsychologyList.as_view(), name='psychology-list'),
    path('test-commit/', TestCommitList.as_view(), name='test-commit-list'),
]
