from django.contrib import admin
from .models import Event
from django.utils.translation import gettext_lazy as _


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('initiator', 'level_display', 'timestamp', 'event',)
    search_fields = ('initiator', 'event', )
    list_filter = ('level', 'timestamp', 'initiator', )

    def level_display(self, obj):
        return obj.level_label

    level_display.short_description = _('Level')

    def get_readonly_fields(self, request, obj=None):
        return [i.name for i in obj._meta.get_fields()]

    def has_add_permission(self, request):
        return False
