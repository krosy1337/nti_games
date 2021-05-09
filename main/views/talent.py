import json

import requests
from django.shortcuts import redirect, reverse

from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from ..models import CsResult, DotaResult, OverwatchResult, TalantUser

from django.conf import settings

from rest_framework.views import APIView

from dataclasses import dataclass

from authlib.integrations.requests_client import OAuth2Session

import time

from .utils import generate_uri, authenticate


@dataclass
class TalentInfo:
    id: int
    email: str
    first_name: str
    last_name: str


def get_talent_info(token) -> TalentInfo:
    client = OAuth2Session(settings.TALENT_CLIENT_ID, settings.TALENT_CLIENT_SECRET, token=token)
    # id, email, first_name, last_name
    resp = client.get('https://talent.kruzhok.org/api/users/me').json()
    return TalentInfo(id=resp['id'], email=resp['email'], first_name=resp['first_name'], last_name=resp['last_name'])


def register_user(talent_info: TalentInfo, token):
    user = User(email=talent_info.email, username=talent_info.email, first_name=talent_info.first_name,
                last_name=talent_info.last_name, id=talent_info.id)
    user.save()

    cs_result = CsResult()
    dota_result = DotaResult()
    overwatch_result = OverwatchResult()

    cs_result.save()
    dota_result.save()
    overwatch_result.save()

    talent_user = TalantUser(user=user, access_token=json.dumps(token), cs_result=cs_result,
                             dota_result=dota_result, overwatch_result=overwatch_result)
    talent_user.save()


class AuthLoginTalent(APIView):
    def get(self, request):
        redirect_uri = generate_uri(request, reverse('authcomplete'))

        uri, state = OAuth2Session(settings.TALENT_CLIENT_ID, settings.TALENT_CLIENT_SECRET,
                                   token_endpoint_auth_method='client_secret_post').create_authorization_url(
            settings.TALENT_AUTHORIZATION_ENDPOINT, response_type='code',
            nonce=time.time(), redirect_uri=redirect_uri
        )

        return redirect(uri)


class AuthCompleteTalent(APIView):
    def get(self, request):
        if request.query_params.get('error'):
            return redirect('home')

        token = requests.post(settings.TALENT_TOKEN_ENDPOINT, data={
            'grant_type': 'authorization_code',
            'scope': 'openid',
            'nonce': time.time(),
            'client_id': settings.TALENT_CLIENT_ID,
            'client_secret': settings.TALENT_CLIENT_SECRET,
            'redirect_uri': generate_uri(request, reverse('authcomplete')),
            'code': request.query_params['code'],
        }).json()

        user_info = get_talent_info(token)

        if not User.objects.filter(email=user_info.email).exists():
            register_user(user_info, token)

        user = authenticate(request, email=user_info.email)

        if user is not None:
            login(request, user)
            return redirect('user')
        return redirect('home')


class LogoutTalent(APIView):
    def get(self, request):
        logout(request)
        return redirect('home')
