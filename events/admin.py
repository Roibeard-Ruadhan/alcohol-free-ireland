from django.contrib import admin
from .models import events
# Register your models here.
admin.site.register(events)

    # def approve_events(self, request, queryset):
    #     queryset.update(approved=True)