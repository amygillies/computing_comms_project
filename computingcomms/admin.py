# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from computingcomms.models import ForumPost, Comment, UserProfile, ADS2Score, WAD2Score, OOSE2Score, AF2Score, CS2TScore, JP2Score
# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('question','picture','date','user')

class Jp2Admin(admin.ModelAdmin):
    list_display = ('user', 'jp2score')

class Ads2Admin(admin.ModelAdmin):
    list_display = ('user', 'ads2score')

class Wad2Admin(admin.ModelAdmin):
    list_display = ('user', 'wad2score')

class Af2Admin(admin.ModelAdmin):
    list_display = ('user', 'af2score')

class Oose2Admin(admin.ModelAdmin):
    list_display = ('user', 'oose2score')

class Cs2tAdmin(admin.ModelAdmin):
    list_display = ('user', 'cs2tscore')


admin.site.register(ForumPost, ForumAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(JP2Score, Jp2Admin)
admin.site.register(AF2Score, Af2Admin)
admin.site.register(CS2TScore, Cs2tAdmin)
admin.site.register(ADS2Score, Ads2Admin)
admin.site.register(OOSE2Score, Oose2Admin)
admin.site.register(WAD2Score, Wad2Admin)
