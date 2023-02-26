from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verbose_name = "Direct Messages"


# 카테고리의 이름을 변경하고 싶을 때는 app.py 에서 verbose_name 으로 수정
