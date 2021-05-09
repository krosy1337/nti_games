from urllib.parse import urlencode

from django.shortcuts import redirect, reverse

from django.conf import settings

from .utils import generate_uri

from rest_framework.views import APIView


class AuthLoginSteam(APIView):
    def get(self, request):
        redirect_uri = generate_uri(request, reverse('steam_auth'))
        params = {
            'openid.ns': settings.OPEN_ID_NS,
            'openid.identity': settings.OPEN_ID_IDENTITY,
            'openid.claimed_id': settings.OPEN_ID_CLAIMED_ID,
            'openid.mode': 'checkid_setup',
            'openid.return_to': redirect_uri,
            'openid.realm': generate_uri(request, reverse('home')),
        }

        auth_url = settings.FORMAT_STEAM_AUTH_URL.format(urlencode(params))
        return redirect(auth_url)


class AuthCompleteSteam(APIView):
    def get(self, request):
        request.user.talantuser.steam_openid = request.query_params['openid.identity']
        request.user.talantuser.steam_id = int(request.query_params['openid.identity'].split('/')[-1])
        request.user.talantuser.save()

        return redirect('user')


class LogoutSteam(APIView):
    def get(self, request):
        request.user.talantuser.steam_openid = ''
        request.user.talantuser.steam_id = None
        request.user.talantuser.save()

        request.user.talantuser.cs_result.result = False
        request.user.talantuser.cs_result.result_str = None
        request.user.talantuser.dota_result.result = False
        request.user.talantuser.dota_result.result_str = None

        request.user.talantuser.cs_result.save()
        request.user.talantuser.dota_result.save()

        return redirect('user')
