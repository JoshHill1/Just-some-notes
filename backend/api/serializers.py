# from rest_framework import serializers
# from .models import Subject

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject         # slug is here in case of making changes to have the cards direct the user to another URL
#         fields = ['id', 'title', 'slug', 'header', 'content', 'image', 'created_at']
from rest_framework import serializers
from .models import Statistics

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['id', 'header', 'content', 'image1', 'image2']