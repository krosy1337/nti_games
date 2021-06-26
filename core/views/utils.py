from django.conf import settings


def generate_uri(request, rev):
    uri = request.build_absolute_uri(rev)

    return uri
