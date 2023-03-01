from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):  # request 객체는 API view 이기 때문에 data가 존재함

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
        # all_categories = Category.objects.all()
    elif request.method == "POST":
        print(request.data)
        return Response({"created": True})


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)  # 카테고리는 하나만 보내고 있어서 many=True 사용 안해도 됨.
    return Response(serializer.data)
