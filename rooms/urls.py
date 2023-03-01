from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    # path("", ~~) 라고 적은 이유는 rooms 폴더 안에 있는 파일이기 때문에 빈 공간이 rooms를 나타내기 때문
    path("<int:room_id>/", views.see_one_room),
    # path("<str:room_name",views.hello), // url에서 문자로 이동하고 싶으면 str 사용 / 숫자는 위에서 int 사용함
]
