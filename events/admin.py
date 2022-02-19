from django.contrib import admin
from .models import events
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    actions = ['approve_events']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)
admin.site.register(events, EventAdmin)

    # def approve_events(self, request, queryset):
    #     queryset.update(approved=True)