from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Award)
admin.site.register(User)
admin.site.register(YearOrder)
admin.site.register(AwardOrder)