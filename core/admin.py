from django.contrib import admin
from .models import TalantUser, CsResult, DotaResult


admin.site.register(CsResult)
admin.site.register(DotaResult)

@admin.register(TalantUser)
class TalantUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'cs_result', 'dota_result')
