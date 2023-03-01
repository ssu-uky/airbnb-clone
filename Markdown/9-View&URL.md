# config > urls.py
urlpatterns = [path ("admin/"), admin.site.urls]
> "admin/" 로 접근하면 admin.site.urls 함수를 실행

from django.http import HttpResponse
 > return값이 string일 경우 이걸 사용해야함

두 가지 방법
1. config > urls.py 에 모든 폴더의 url 생성하고 연결하기
  > config > urls.py 파일 상단에 from / import 를 일일히 해줘야함
  > 파일이 정신없어짐 

2. ⭐️ 모든 폴더에 urls.py 파일 생성하기 ⭐️
모든 폴더에 각각 urls.py 파일을 생성한 후 config > urls.py 에서 하나로 합치기


# views.py - 유저가 특정 url에 접근했을 때 작동하게 되는 함수가 있는 파일
(views.py 는 다른 파일들과 다르게 views의 이름을 변경해도 된다. 다른 파일들은 장고에서 찾지 못하므로 절대 안됨.)

def 로 실행 될 함수를 생성해 준 다음 request로 받는다.
template을 만들어서 안에 {{ 변수명 }} 을 넣어주면 댐.
{% for room in rooms %} / {% endfor %}