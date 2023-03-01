# 1. python manage.py startapp 폴더명
# 2. 폴더명으로 폴더가 만들어짐
# 3. config > setting 가서 CUSTOM_APPS에 앱 추가 - ( 소문자이름.apps.class 이름(대문자시작) 폴더의 app.py 가서 class 폴더명.Config)
# 4. models.py
  1) 의류 - 상단에 from common.models import CommonModel 선언
# 의류 소개 class
  1-1) 상의 -   class 상의(CommonModel):
  1-2) 맨투맨 -   class 맨투맨(models.여긴 주제(맨투맨)에 따라서 정하기)"
  1-3) 크롭핏/레귤러핏/오버핏 - 주제에서 세분화 될 내용들

 2) 바지 = models.TextChoices / CharField (글자 길이, 기본값 등 정하기 )
  상속 받을 위치가 있다면 같이 적어주기

# 5. admin.py
  1) 상단에 from .models import 상속받을위치
  2) @admin.register(위에서 선언 한 상속받을위치)
  3) list_display / list_filter 작성

# 6. python manage.py makemigrate
# 7. python manage.py migration
