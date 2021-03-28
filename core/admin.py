from django.contrib import admin
from django.contrib.sessions.models import Session

from core.models import Url


class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'url_subpart', 'created_at')


class SessionModelAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'expire_date')
    readonly_fields = ('session_key', 'session_data', 'expire_date')


admin.site.register(Url, UrlModelAdmin)
admin.site.register(Session, SessionModelAdmin)
