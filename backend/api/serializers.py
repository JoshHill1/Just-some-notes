from rest_framework import serializers
from .models import Statistics

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'header', 'content', 'image1', 'image2']