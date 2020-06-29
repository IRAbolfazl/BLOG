from django.contrib import admin
from .models import *

class userprofileadmin(admin.ModelAdmin):
    list_display = ['user','avatar','descripion']

admin.site.register(userprofile,userprofileadmin)

class userarticle(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ['title','cover','creat_at']

admin.site.register(article,userarticle)