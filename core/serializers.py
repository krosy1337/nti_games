from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TalantUser, DotaResult, CsResult


class CsResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsResult
        fields = (
            'error', 'result',
            'result_num', 'result_str',
            'result_big_str', 'result_json',
        )


class DotaResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DotaResult
        fields = (
            'error', 'result',
            'result_num', 'result_str',
            'result_big_str', 'result_json',
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # 'username',
            'email',
            'id',
            'first_name',
            'last_name'
        )


class TalentUserSerializer(serializers.ModelSerializer):
    dota_result = DotaResultSerializer()
    cs_result = CsResultSerializer()

    class Meta:
        model = TalantUser
        fields = (
            'pk', 'steam_id',
            'dota_result', 'cs_result',
            'dota_task', 'cs_task',
        )
