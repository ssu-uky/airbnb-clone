from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private_room")
        SHARED_ROOM = "shared_room", "Shared_room"

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",  # 접근자를 커스텀마이징 시킴
    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(room):  # room인 이유는 self 를 그냥 room으로 칭햇음 여기서는 self가 room인 것
        return room.amenities.count()

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "리뷰 없음"
        else:
            total_rating = 0
            for review in room.reviews.all().values(
                "rating"
            ):  # valus로 원하는 값만 가져옴 / values를 사용하면 코드가 망가져서 고쳐야 함
                total_rating += review["rating"]
            return round(total_rating / count, 2)  # 소숫점 2자리까지 나타내는 반올림함수 round 사용


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
