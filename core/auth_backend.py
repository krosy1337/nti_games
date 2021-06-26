from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class OAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, **kwargs):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
