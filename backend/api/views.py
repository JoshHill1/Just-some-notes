# from django.shortcuts import render

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

# @api_view(['GET'])
# def Statistics(request):
#     return Response({"message": "This is Statistics content from Django."})

# @api_view(['GET'])
# def PublicSpeaking(request):
#     return Response({"message": "This is Public Speaking content from Django."})

# @api_view(['GET'])
# def Business(request):
#     return Response({"message": "This is Business content from Django."})

# @api_view(['GET'])
# def Psychology(request):
#     return Response({"message": "This is Psychology content from Django."})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Page

def get_page_data(page_number):
    try:
        page = Page.objects.get(page_number=page_number)
        data = {
            "header": page.header,
            "content": page.content,
            "image1": page.image1.url if page.image1 else None,
            "image2": page.image2.url if page.image2 else None,
        }
        return data
    except Page.DoesNotExist:
        raise Http404("Page not found")

@api_view(['GET'])
def page1(request):
    data = get_page_data(1)
    return Response(data)

@api_view(['GET'])
def page2(request):
    data = get_page_data(2)
    return Response(data)

@api_view(['GET'])
def page3(request):
    data = get_page_data(3)
    return Response(data)

@api_view(['GET'])
def page4(request):
    data = get_page_data(4)
    return Response(data)




# @api_view(['GET'])
# def hello_world(request):
#     data = get_page_data(1)
#     return Response(data)

# @api_view(['GET'])
# def statistics(request):
#     data = get_page_data(2)
#     return Response(data)

# @api_view(['GET'])
# def publicSpeaking(request):
#     data = get_page_data(3)
#     return Response(data)

# @api_view(['GET'])
# def business(request):
#     data = get_page_data(4)
#     return Response(data)

# @api_view(['GET'])
# def psychology(request):
#     data = get_page_data(5)
#     return Response(data)
