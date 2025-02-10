from rest_framework.generics import ListAPIView
from .models import Statistics
from .serializers import StatisticsSerializer

class StatisticsList(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
