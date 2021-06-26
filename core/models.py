from django.db import models
from django.contrib.auth.models import User


class DotaResult(models.Model):
    error = models.CharField(max_length=200, default=None, null=True)
    result = models.BooleanField(default=False)
    result_num = models.BigIntegerField(default=None, null=True)
    result_str = models.CharField(max_length=250, default=None, null=True)
    result_big_str = models.CharField(max_length=1000, default=None, null=True)
    result_json = models.CharField(max_length=5000, default=None, null=True)

    def __str__(self):
        return f'{str(self.result_num)} | {self.pk}'


class CsResult(models.Model):
    error = models.CharField(max_length=200, default=None, null=True)
    result = models.BooleanField(default=False)
    result_num = models.BigIntegerField(default=None, null=True)
    result_str = models.CharField(max_length=250, default=None, null=True)
    result_big_str = models.CharField(max_length=1000, default=None, null=True)
    result_json = models.CharField(max_length=5000, default=None, null=True)

    def __str__(self):
        return f'{str(self.result_num)} | {self.pk}'


class TalantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=2500)

    steam_openid = models.CharField(max_length=200, default=None, null=True)
    steam_id = models.BigIntegerField(default=None, null=True)
    steam_username = models.CharField(max_length=200, default=None, null=True)

    dota_result = models.OneToOneField(DotaResult, on_delete=models.CASCADE, default=None, null=True)
    dota_task = models.CharField(max_length=100, default=None, null=True)

    cs_result = models.OneToOneField(CsResult, on_delete=models.CASCADE, default=None, null=True)
    cs_task = models.CharField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.user.username
