from django.urls import path, include

from analytics.csgo import algo_csgo
from analytics.dota import algo_dota
from analytics.overwatch import algo_overwatch


from .views import analyse, pages, steam, talent, blizzard


urlpatterns = [
    path('', pages.home, name='home'),
    path('user', pages.user, name='user'),


    path('authlogin', talent.AuthLoginTalent.as_view(), name='authlogin'),
    path('authcomplete', talent.AuthCompleteTalent.as_view(), name='authcomplete'),
    path('logout', talent.LogoutTalent.as_view(), name='logout'),

    path('steam_login', steam.AuthLoginSteam.as_view(), name="steam_login"),
    path('steam_auth', steam.AuthCompleteSteam.as_view(), name="steam_auth"),
    path('logout_steam', steam.LogoutSteam.as_view(), name='logout_steam'),


    path('blizzard_login', blizzard.AuthLoginBlizzard.as_view(), name='blizzard_login'),
    path('blizzard_authn', blizzard.AuthCompleteBlizzard.as_view(), name='blizzard_auth'),
    path('blizzard_logout', blizzard.LogoutBlizzard.as_view(), name='blizzard_logout'),


    path('analyse_csgo', algo_csgo.csgo_start_analysing, name="analyse_csgo"),
    path('analyse_dota', algo_dota.dota_start_analysing, name="analyse_dota"),
    path('analyse_overwatch', algo_overwatch.overvatch_start_analysing, name="analyse_overwatch"),
]