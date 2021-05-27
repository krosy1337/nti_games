import requests
from django.shortcuts import redirect, reverse

from authlib.integrations.requests_client import OAuth2Session

from rest_framework.views import APIView

from django.conf import settings

from .utils import generate_uri



class AuthLoginBlizzard(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        redirect_uri = generate_uri(request, reverse('blizzard_auth'))

        uri, state = OAuth2Session(settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_id'],
                                   settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_secret']).create_authorization_url(
            settings.BLIZZARD_API_AUTHORIZE_URL, response_type='code', redirect_uri=redirect_uri)

        return redirect(uri)


class AuthCompleteBlizzard(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        token = requests.post(settings.BLIZZARD_API_TOKEN_URL, data={
            'grant_type': 'authorization_code',
            'scope': 'openid',
            'client_id': settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_id'],
            'client_secret': settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_secret'],
            'redirect_uri': generate_uri(request, reverse('blizzard_auth')),
            'code': request.query_params['code'],
        }).json()

        client = OAuth2Session(settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_id'],
                               settings.AUTHLIB_OAUTH_CLIENTS['blizzard']['client_secret'], token=token)
        resp = client.get(settings.BLIZZARD_API_USERINFO_URL).json()

        request.user.talantuser.blizzard_id = resp['id']
        request.user.talantuser.blizzard_battletag = resp['battletag']

        request.user.talantuser.save()

        return redirect('user')


class LogoutBlizzard(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        request.user.talantuser.blizzard_access_token = None
        request.user.talantuser.blizzard_battletag = None
        request.user.talantuser.blizzard_id = None
        request.user.talantuser.overwatch_result.result = False
        request.user.talantuser.overwatch_result.result_str = None

        request.user.talantuser.save()
        request.user.talantuser.overwatch_result.save()

        return redirect('user')
