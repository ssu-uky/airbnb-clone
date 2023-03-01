## ORM : 저장 된 정보들을 admin패널에서 관리하지않고 직접 관리할 수 있는 시스템

###   python manage.py shell  ###

## ⭐️ from rooms.models import Room ⭐️ ## > Room으로 데이터 찾을 경우

## ⭐️ from users.models import User ⭐️ ## > User 로 데이터 찾을 경우
연결 되어 있는 상태에서 터미널 창 비우기
print("\033c", end='')

# 원하는 카테고리로 이동하고 싶다면 model을 이용해서 접근
Room.objects.all() > Room의 모든 객체를 보여줌
room = Room.objects.get(name="Beautiful View")
room의 값을 설정해주면 설정해 준 값으로 데이터를 찾고 변경하고 지울 수 있음 > Foreignkey 로 접근

# .get() 은 하나의 model과 하나의 data만 반환 가능
.get의 결과값은 무조건 하나여야한다. / 특별한 것을 찾을 때 사용 / ex)pet_friendly 같은 경우에는 두 방에 값이 들어가있으므로 .get으로 찾을 수 없음

# Room.objects.filter(price__gt=30) 
gt (greater than) : >
lt (less than) : <
gte (greater than or equal) : >=
lte (less than or equal) : <=

## from rooms.models import Amenity ##
Room.objects.get(pk=1).total_amenities() > 1번 방의 모든 어메니티 호출

# room -> admin.py 
def total_amenities(self, room):
        return room.amenities.count() > 각 룸의 어메니티 개수를 호출
  # models.py 에서 호출 시
  def total_amenities(self):
        return self.amenities.count() > 각 룸의 어메니티 개수를 호출

어메니티의 갯수 호출방법은 위 처럼 두 가지가 있음

Room 을 전부 찾으려면 user는 무조건 하나 이상 업로드 되어 있어야한다 (연결되어있기때문)


## ⭐️ from users.models import User ⭐️ ## > User 로 데이터 찾을 경우
me = user.objects.get(pk=1)
me를 정의해줌

user로 찾을 경우 !
dir(me)
라고 하면 me에서 사용 가능 한 user 가 가지고 있는 메소드와 속성들을 보여줌 ( _set )

# 접근자를 커스터마이징 하기
models.py 폴더에서 링크(연결)되어 있는 친구들에게 새롭게 커스터마이징을 해줌.
experience = models.ForeignKey(
        "experiences.Experience", #이런 식으로 연결되어 있는 곳에
        related_name="experiences", 로 이름을 새로 붙혀줌
        )
rooms > models.py > owner, amenities, category 에 related_name을 추가해줌
makemigrations > migrate