# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    details = models.CharField(max_length=256)
    

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username

class ForumPost(models.Model):
    question = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='forum_images',blank=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(ForumPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

class Comment(models.Model):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='comment_images', blank=True)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('computingcomms.ForumPost', related_name = 'comment' , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user + " posted to " + self.post
    
class JP2Score(models.Model):
    jp2score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

class CS2TScore(models.Model):
    cs2tscore = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

class ADS2Score(models.Model):
    ads2score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

class AF2Score(models.Model):
    af2score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

class OOSE2Score(models.Model):
    oose2score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)

class WAD2Score(models.Model):
    wad2score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user)
