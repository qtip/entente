from django.contrib import admin

# Register your models here.
from .models import Server, Channel

# Register your models here.
admin.site.register(Server)
admin.site.register(Channel)