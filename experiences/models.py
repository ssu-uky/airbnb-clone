from django.db import models
from common.models import CommonModel

# from categories.models import Category

# Create your models here.
class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )

    city = models.CharField(
        max_length=80,
        default="서울",
    )

    name = models.CharField(
        max_length=250,
    )

    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )

    price = models.PositiveIntegerField()

    address = models.CharField(
        max_length=250,
    )

    start = models.TimeField()
    end = models.TimeField()

    description = models.TextField()

    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        # on_delete = models.CASCADE 는 카테고리가 삭제되면 experiences 가 삭제된다는 뜻 / 그래서 SET_NULL 사용
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self) -> str:
        return self.name


# Experience 에서 Perk는 여러개 가질 수 있다.
class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        # null = True 도 가능 // default = "" 와 같은 것
        default="",
    )
    # detail 의 설명
    explanation = models.TextField(
        blank=True,
        # null = True 도 가능 // default = "" 와 같은 것
        null=True,
    )

    def __str__(self) -> str:
        return self.name
