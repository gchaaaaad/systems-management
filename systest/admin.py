from django.contrib import admin
from .models import System, Version, Module, TestOverview


admin.site.register(System)
admin.site.register(Version)
admin.site.register(Module)
admin.site.register(TestOverview)
