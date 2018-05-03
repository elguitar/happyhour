from django.contrib import admin
from .models import Bar, HappyHour, HappyHourInstance

admin.site.register(Bar)
admin.site.register(HappyHour)
admin.site.register(HappyHourInstance)
