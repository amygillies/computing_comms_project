# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from computingcomms.models import Quiz, Question, ForumPost, Comment, UserProfile, Answer

# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('question','picture','date','user')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name','quizID','subject')


    
admin.site.register(ForumPost, ForumAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(UserProfile)
