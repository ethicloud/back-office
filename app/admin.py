from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Organization)
admin.site.register(Instance)
