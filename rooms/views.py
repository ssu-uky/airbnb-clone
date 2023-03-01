from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# /rooms 에 접근 했을 때 실행 될 함수 생성
def see_all_rooms(request):
    rooms = Room.objects.all()


def see_one_room(request, room_id):
    return HttpResponse(f"See room with id: {room_id}")
