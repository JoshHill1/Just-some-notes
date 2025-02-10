from rest_framework import serializers
from .models import Statistics, PublicSpeaking, Business, Psychology

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'header', 'sub_text', 'content', 'image1', 'image2']


class PublicSpeakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicSpeaking
        fields = ['id', 'header', 'sub_text', 'content', 'image1', 'image2']


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'header', 'sub_text', 'content', 'image1', 'image2']


class PsychologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Psychology
        fields = ['id', 'header', 'sub_text', 'content', 'image1', 'image2']