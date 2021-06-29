import json
from urllib.parse import urlencode

import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from core.views.utils import generate_uri


class AuthLoginSteam(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        redirect_uri = generate_uri(request, reverse('steam_auth'))
        params = {
            'openid.ns': settings.OPEN_ID_NS,
            'openid.identity': settings.OPEN_ID_IDENTITY,
            'openid.claimed_id': settings.OPEN_ID_CLAIMED_ID,
            'openid.mode': 'checkid_setup',
            'openid.return_to': redirect_uri,
            'openid.realm': generate_uri(request, reverse('index')),
        }

        auth_url = settings.FORMAT_STEAM_AUTH_URL.format(urlencode(params))
        return redirect(auth_url)


class AuthCompleteSteam(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.talantuser.steam_openid = request.query_params['openid.identity']
        request.user.talantuser.steam_id = int(request.query_params['openid.identity'].split('/')[-1])
        response = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={settings.STEAM_API_KEY}&steamids={request.user.talantuser.steam_id}').text)
        request.user.talantuser.steam_username = response['response']['players'][0]['personaname']
        request.user.talantuser.save()
        # <QueryDict: {
        #   'openid.ns': ['http://specs.openid.net/auth/2.0'],
        #   'openid.mode': ['id_res'],
        #   'openid.op_endpoint': ['https://steamcommunity.com/openid/login'],
        #   'openid.claimed_id': ['https://steamcommunity.com/openid/id/76561198247304156'],
        #   'openid.identity': ['https://steamcommunity.com/openid/id/76561198247304156'],
        #   'openid.return_to': ['http://localhost:8000/steam/auth'],
        #   'openid.response_nonce': ['2020-12-07T14:30:09ZTQ2iswQERox0QdJj3z7TaJyaSHk='],
        #   'openid.assoc_handle': ['1234567890'],
        #   'openid.signed': ['signed,op_endpoint,claimed_id,identity,return_to,response_nonce,assoc_handle'],
        #   'openid.sig': ['TWCPNyTh59oRkjUr2ei392alTfM=']}>
        return redirect('user_page')


class LogoutSteam(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.talantuser.steam_openid = ''
        request.user.talantuser.steam_id = None
        request.user.talantuser.cs_result.result = False
        request.user.talantuser.cs_result.result_num = None
        request.user.talantuser.cs_result.result_str = None
        request.user.talantuser.cs_result.result_big_str = None
        request.user.talantuser.cs_result.result_json = None
        request.user.talantuser.cs_result.error = None

        request.user.talantuser.dota_result.result = False
        request.user.talantuser.dota_result.result_num = None
        request.user.talantuser.dota_result.result_str = None
        request.user.talantuser.dota_result.result_big_str = None
        request.user.talantuser.dota_result.result_json = None
        request.user.talantuser.dota_result.error = None
        request.user.talantuser.cs_result.save()
        request.user.talantuser.dota_result.save()
        request.user.talantuser.save()

        return redirect('user_page')
