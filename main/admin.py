from django.contrib import admin
from .models import TalantUser, DotaResult, OverwatchResult, CsResult
# Register your models here.

admin.site.register(TalantUser)
admin.site.register(DotaResult)
admin.site.register(OverwatchResult)
admin.site.register(CsResult)


