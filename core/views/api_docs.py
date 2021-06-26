from django.shortcuts import redirect
from rest_framework.decorators import api_view


@api_view()
def schema_view(request):
    return redirect('/static/core/schema.yml')
