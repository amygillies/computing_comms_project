# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.test import TestCase
import os

from computingcomms.models import ForumPost


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

        # Check if is there an image in index page
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
        
