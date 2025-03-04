from rest_framework.generics import ListAPIView
from .models import Statistics, PublicSpeaking, Business, Psychology, TestCommit
from .serializers import StatisticsSerializer, PublicSpeakingSerializer, BusinessSerializer, PsychologySerializer, TestCommitSerializer

class StatisticsList(ListAPIView):
    queryset = Statistics.objects.all().order_by('-id')
    serializer_class = StatisticsSerializer

class PublicSpeakingList(ListAPIView):
    queryset = PublicSpeaking.objects.all().order_by('-id')
    serializer_class = PublicSpeakingSerializer

class BusinessList(ListAPIView):
    queryset = Business.objects.all().order_by('-id')
    serializer_class = BusinessSerializer

class PsychologyList(ListAPIView):
    queryset = Psychology.objects.all().order_by('-id')
    serializer_class = PsychologySerializer

class TestCommitList(ListAPIView):
    queryset = TestCommit.objects.all().order_by('-id')
    serializer_class = TestCommitSerializer