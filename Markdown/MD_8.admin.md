# rooms > admin.py
search_fields = ("name","price",) > 튜플로 작성하기
__startswith (첫 글자로 검색하고 싶을 때는)
  > search_fields = ("^name","^price") 원하는 필터 앞에 ^ 넣기

정확한 검색을 원할 때는
  > search_fields = ("=name","=price") 원하는 필터 앞에 = 넣기

# @admin.action(description="추가할 액션의 내용")
액션은 3개의 매개변수가 필요 (model_admin, request, queryset)
# def reset_price(model_admin,request, queryset)
1. model_admin = 액션을 가지고 있는 model_admin을 호출
(하단 register(room)에 action 추가해주기)
actions = (reset_prices,)
2. request =  누가 호출했는지에 대한 정보를 가지고 있음
(액션을 요청하는 user에 대한 정보를 가지고 있음)
3. queryset = 내가 선택한 요소들 (room의 목록들)
  > 여기서는 rooms로 입력해 줌(원하는 문구 가능)
  > for room in rooms:
        room.price = 0
        room.save()
    의 함수를 넣음으로써 이 액션이 실행 된 room은 price가 0으로 변함

## 정리 ##
@admin.action(description = "원하는 액션 문구")
def 함수 생성 ():
  for room in rooms.all(model_admin, request, rooms)"
      room.price = 0
      room.save()
      
  > 이렇게 함수를 만들어주면 액션 생성 완료


  # 필터를 직접 만들고 싶을 때 #
  review > admin.py
  class 이름(admin.SimpleListFilter):

    title = "필터 제목"
    parameter_name = "필터링 할 요소" (url에 표시 됨)

    def lookups(self, request, model_admin):
      return [
        ("good", "Good"), // good은 url에 표시되는 요소 , Good은 사용자가 보는 요소
        ("great", "Great"),
        ("awesome", "Awesome"),
      ]
  lookups 은 튜플의 리스트를 리턴해야하는 함수인데 튜플의 첫번째 요소는 url에 나타나게 되고, 두번째 요소는 유저가 볼 수 있는 요소

    def queryset(self, request, reviews):
querset은 필터링 된 reviews를 리턴해야하는 메소드
    word = self.value() > url에 있는 단어 보여줌

    if word:
      return reviews.filter(payload__contains=word)
    else:
      reviews