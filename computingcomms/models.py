# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=32)
    quizID = models.CharField(max_length=4)
    subject = models.CharField(max_length=4)

    def __str__(self):
        return self.subject
    
class Question(models.Model):
    name = models.CharField(max_length=128,unique=True)
    content = models.CharField(max_length=256)
    quiz = models.ForeignKey(Quiz)

    def __str__(self):
        return self.name

class Answer(models.Model):
    answerID = models.CharField(max_length=4, unique=True)
    content = models.CharField(max_length=256)
    correct = models.BooleanField(default = False)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.answerID

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    details = models.CharField(max_length=256)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username

class ForumPost(models.Model):
    question = models.CharField(max_length=128)
    image = models.ImageField(upload_to='forum_images',blank=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user

class Comment(models.Model):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='comment_images', blank=True)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(ForumPost)

    def __str__(self):
        return self.user + " posted to " + self.post
    
