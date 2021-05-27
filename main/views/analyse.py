from django.shortcuts import redirect

import random

phrases = ["Отличный", "Хороший", "Средний", "Плохой"]


def analyse_csgo(request):
    if not request.user.is_authenticated:
        return redirect('home')
    request.user.talantuser.cs_result.result = True
    request.user.talantuser.cs_result.result_str = f'{random.choice(phrases)} уровень командности'
    request.user.talantuser.cs_result.save()
    return redirect('user')


def analyse_dota(request):
    if not request.user.is_authenticated:
        return redirect('home')
    request.user.talantuser.dota_result.result = True
    request.user.talantuser.dota_result.result_str = f'{random.choice(phrases)} уровень командности'
    request.user.talantuser.dota_result.save()
    return redirect('user')


def analyse_overwatch(request):
    if not request.user.is_authenticated:
        return redirect('home')
    request.user.talantuser.overwatch_result.result = True
    request.user.talantuser.overwatch_result.result_str = f'{random.choice(phrases)} уровень командности'
    request.user.talantuser.overwatch_result.save()
    return redirect('user')
