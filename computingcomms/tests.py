# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.test import TestCase
import os

from computingcomms.models import ForumPost, Comment
from django.contrib.auth.models import User


class CommsTests(TestCase):

    def test_view_has_title(self):
        response = self.client.get(reverse('home'))

        #Check title used correctly
        self.assertIn('<title>', response.content.decode('ascii'))
        self.assertIn('</title>', response.content.decode('ascii'))

    def test_home_using_template(self):
        response = self.client.get(reverse('home'))

        # Check the template used to render index page
        self.assertTemplateUsed(response, 'computingcomms/home.html')

    def test_quizzes_using_template(self):
        self.client.get(reverse('home'))
        response = self.client.get(reverse('quizzes'))

        # Check the template used to render about page
        self.assertTemplateUsed(response, 'computingcomms/quizzes.html')

    def test_using_CSS(self):
        response = self.client.get(reverse('home'))

        # Check if is there an attempt to use CSS
        self.assertIn('type="text/css"'.lower(), response.content.decode('ascii').lower())

    def test_register_uses_form(self):
        self.client.get(reverse('home'))
        response = self.client.get(reverse('register'))

        self.assertIn('enctype = "multipart/form-data"', response.content.decode('ascii'))
        self.assertIn('</form>', response.content.decode('ascii'))

    def test_login_has_user_and_pass(self):
        self.client.get(reverse('home'))
        response = self.client.get(reverse('login'))

        self.assertIn('<input type="text" name="username"', response.content.decode('ascii'))
        self.assertIn('<input type="password" name="password"', response.content.decode('ascii'))

    def test_forum_post(self):
        user = User.objects.get_or_create(username="Test",password="testpass")[0]
        post = ForumPost.objects.get_or_create(question="This is my test.",user=user)[0]
        post.save()

        posts_in_db = ForumPost.objects.all()
        self.assertEquals(len(posts_in_db), 1)
        only_post = posts_in_db[0]
        self.assertEquals(post,only_post)

    def test_comment_on_post(self):
        user = User.objects.get_or_create(username="Test",password="testpass")[0]
        post = ForumPost.objects.get_or_create(question="This is my test.",user=user)[0]
        post.save()
        
        user2 = User.objects.get_or_create(username="OtherTest",password="guessme")[0]
        FirstComment = Comment()
        FirstComment.comment="What an easy question, did you even google it?"
        FirstComment.user = user2
        FirstComment.post = post
        FirstComment.save()

        SecondComment = Comment()
        SecondComment.comment="I'm not very good aat this... :( "
        SecondComment.user = user
        SecondComment.post = post
        SecondComment.save()

        comments = Comment.objects.filter(post=post)
        self.assertEquals(len(comments), 2)
        self.assertEquals(comments[0],FirstComment)
        self.assertEquals(comments[1],SecondComment)
        

    def test_post_slugs(self):
        user = User.objects.get_or_create(username="Test",password="testpass")[0]
        post = ForumPost.objects.get_or_create(question="What is a slug?",user=user)[0]
        post.save()

        self.assertEquals(post.slug,"what-is-a-slug")
