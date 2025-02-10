from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Page

def get_page_data(page_number):
    try:
        page = Page.objects.get(page_number=page_number)
    except Page.DoesNotExist:
        raise Http404("Page not found")
    data = {
        "header": page.header,
        "content": page.content,
        "image1": page.image1.url if page.image1 else None,
        "image2": page.image2.url if page.image2 else None,
    }
    return data

@api_view(['GET'])
def statistics(request):
    data = get_page_data(1)
    return Response(data)

@api_view(['GET'])
def public_speaking(request):
    data = get_page_data(2)
    return Response(data)

@api_view(['GET'])
def business(request):
    data = get_page_data(3)
    return Response(data)

@api_view(['GET'])
def psychology(request):
    data = get_page_data(4)
    return Response(data)
