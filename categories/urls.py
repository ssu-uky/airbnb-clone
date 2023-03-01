from django.urls import path
from . import views

urlpatterns = [
    path("/", views.categories),
    path("/<int:pk>", views.category),  # views.py의 category(함수)에서 pk를 int(정수)로 받겠다
]
