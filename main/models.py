from django.db import models
from django.contrib.auth.models import User

class DotaResult(models.Model):
    result = models.BooleanField(default=False)
    result_str = models.CharField(max_length=2500, default=None, null=True)


class CsResult(models.Model):
    result = models.BooleanField(default=False)
    result_str = models.CharField(max_length=2500, default=None, null=True)


class OverwatchResult(models.Model):
    result = models.BooleanField(default=False)
    result_str = models.CharField(max_length=2500, default=None, null=True)

class TalantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=2500)

    steam_openid = models.CharField(max_length=200, default=None, null=True)
    steam_id = models.BigIntegerField(default=None, null=True)

    blizzard_access_token = models.CharField(max_length=2500, default=None, null=True)
    blizzard_id = models.BigIntegerField(default=None, null=True)
    blizzard_battletag = models.CharField(max_length=100, default=None, null=True)

    cs_result = models.OneToOneField(CsResult, on_delete=models.CASCADE, default=None, null=True)
    dota_result = models.OneToOneField(DotaResult, on_delete=models.CASCADE, default=None, null=True)
    overwatch_result = models.OneToOneField(OverwatchResult, on_delete=models.CASCADE, default=None, null=True)

# Create your models here.
