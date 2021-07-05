import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index_page(request):
    if request.user.is_authenticated:
        return redirect('user_page')
    return render(request, 'core/home.html')


@login_required
def user_page(request):
    games = []
    general_score = 0
    if request.user.talantuser.dota_result.result and not request.user.talantuser.dota_result.error:
        games.append(request.user.talantuser.dota_result.result_num)
    if request.user.talantuser.cs_result.result and not request.user.talantuser.cs_result.error:
        games.append(request.user.talantuser.cs_result.result_num)

    if len(games):
        general_score = int(sum(games)/len(games))
    #or request.user.talantuser.dota_result.error
    return render(request, 'core/user.html', {
        'user': request.user,
        'dota_result': None if (
                    request.user.talantuser.dota_result.result is None or request.user.talantuser.dota_result.result_json is None) else
        json.loads(request.user.talantuser.dota_result.result_json),
        'cs_result': None if (
                    request.user.talantuser.cs_result.result is None or request.user.talantuser.cs_result.result_json is None
                    or request.user.talantuser.cs_result.error) else
        json.loads(request.user.talantuser.cs_result.result_json),
        'general_score': general_score,
    })


def about(request):
    return render(request, 'core/about.html')


def page_not_found(request, exception):
    return render(request, 'core/error.html')
