from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def Statistics(request):
    return Response({"message": "This is Statistics content from Django."})

@api_view(['GET'])
def PublicSpeaking(request):
    return Response({"message": "This is Public Speaking content from Django."})

@api_view(['GET'])
def Business(request):
    return Response({"message": "This is Business content from Django."})

@api_view(['GET'])
def Psychology(request):
    return Response({"message": "This is Psychology content from Django."})
