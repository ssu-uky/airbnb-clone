serializer 는 django python 을 json으로 번역 해주는 역할이지만 그 반대로 해주고,
또한 serializer는 user 에서 온 data를 받아서 데이터베이스에 넣을 수 있는 django 객체로 바꿔줌

{
"name": "Category from DRF",
"kind": "rooms"
}

---------------------------------

REST API를 사용할 때,
폴더 내에 serializers 폴더 생성 후,
# from rest_framework import serializers
# class CategorySerializer(serializer.Serializer):
    모델에 어떤 필드가 있는지 알려주고 어떻게 변환되는지 알려주기

    pk = serializers.IntegerField() > pk를 정수 또는 문자열로 출력
    name = serializers.CharField(required=True) > 필수인지 선택인지 표시 ( 여기서는 True 이기 때문에 필수요소 )
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()

# views.py 가서 urlpatterns 안에 넣기
 path("<int:pk>", views.category) > # views.py의 category(함수)에서 pk를 int(정수)로 받겠다

 # views.py 가서 catagory 함수 설정하기
 
 # urls.py
 path의 주소 앞에 "/~~" 슬ㄹㅐ시 붙히기..

# view.py
 @api_view(["GET", "POST"]) post를 넣어줌으로써 post의 공간이 만들어짐