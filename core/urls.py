from django.urls import path
from .views import api, talent, blizzard, pages, steam, api_docs
from django.views.generic import TemplateView


urlpatterns = [
    path('', pages.index_page, name='index'),
    path('user/', pages.user_page, name='user_page'),

    path('api/auth/login/talent/', talent.AuthLoginTalent.as_view(), name='api_auth_login_talent'),
    path('api/auth/complete/talent/', talent.AuthCompleteTalent.as_view(), name='api_auth_complete_talent'),
    path('api/logout/talent/', talent.LogoutTalent.as_view(), name='logout'),

    path('api/auth/login/steam/', steam.AuthLoginSteam.as_view(), name='steam_login'),
    path('api/auth/complete/steam/', steam.AuthCompleteSteam.as_view(), name='steam_auth'),
    path('api/logout/steam/', steam.LogoutSteam.as_view(), name='steam_logout'),

    path('api/auth/login/blizzard/', blizzard.AuthLoginBlizzard.as_view(), name='blizzard_login'),
    path('api/auth/complete/blizzard/', blizzard.AuthCompleteBlizzard.as_view(), name='blizzard_auth'),
    path('api/logout/blizzard/', blizzard.LogoutBlizzard.as_view(), name='blizzard_logout'),

    path('api/analyse/dota/start/', api.DotaAnalyseStart.as_view(), name='analyse-dota'),
    path('api/analyse/cs/start/', api.CsAnalyseStart.as_view(), name='analyse-cs'),
    path('api/analyse/overwatch/start/', api.OverwatchAnalyseStart.as_view(), name='analyse-overwatch'),
    path('api/analyse/dota/result/', api.CurrentUserDotaResultView.as_view(), name='analyse_dota_result'),
    path('api/analyse/cs/result/', api.CurrentUserCsResultView.as_view(), name='analyse_cs_result'),
    path('api/analyse/overwatch/result/', api.CurrentUserOverwatchResultView.as_view(), name='analyse_overwatch_result'),
    path('api/analyse/status/', api.TaskStatus.as_view(), name='task_status'),

    path('api/user/', api.CurrentUserView.as_view(), ),
    path('api/user/games/', api.CurrentTalentUserView.as_view(), ),

    path('api/docs/schema/', api_docs.schema_view, name='schema_url'),
    path('api/docs/', TemplateView.as_view(
        template_name='core/redoc.html',
    ), name='redoc'),
]
