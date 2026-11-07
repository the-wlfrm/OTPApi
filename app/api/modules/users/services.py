from django.db import transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class UserService:
    @classmethod
    @transaction.atomic
    def create_user(validated_data: dict) -> User:
        user = User.objects.create(**validated_data)
        return user