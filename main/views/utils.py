from django.contrib.auth.models import User

import os

from dotenv import load_dotenv
load_dotenv()


def generate_uri(request, rev):
    uri = request.build_absolute_uri(rev)
    # if (not'https:' in uri) and int(os.environ.get("PRODUCTION")):
    #     uri = uri.replace('http:', 'https:')
    return uri


def authenticate(request, email=None, **kwargs):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None
