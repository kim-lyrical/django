from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import *

#깔끔하게 띄워주는 부분

class AllPacketOption(admin.ModelAdmin):
    list_display = ['id','time','srcip','dstip','protocol','length','info','carve']

admin.site.register(AllPacket,AllPacketOption)