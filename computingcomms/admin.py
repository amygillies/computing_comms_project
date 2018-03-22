# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from computingcomms.models import ForumPost, Comment, UserProfile, ADS2Score, WAD2Score, OOSE2Score, AF2Score, CS2TScore, JP2Score
# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('question','picture','date','user')

class Jp2Admin(admin.ModelAdmin):
    list_display = ('jp2score', 'user')

class Ads2Admin(admin.ModelAdmin):
    list_display = ('ads2score', 'user')

class Wad2Admin(admin.ModelAdmin):
    list_display = ('wad2score', 'user')

class Af2Admin(admin.ModelAdmin):
    list_display = ('af2score', 'user')

class Oose2Admin(admin.ModelAdmin):
    list_display = ('oose2score', 'user')

class Cs2tAdmin(admin.ModelAdmin):
    list_display = ('cs2tscore', 'user')


admin.site.register(ForumPost, ForumAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(JP2Score)
admin.site.register(AF2Score)
admin.site.register(CS2TScore)
admin.site.register(ADS2Score)
admin.site.register(OOSE2Score)
admin.site.register(WAD2Score)
