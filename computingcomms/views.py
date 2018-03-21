# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from computingcomms.models import ForumPost, UserProfile, Comment
from computingcomms.forms import UserForm, UserProfileForm, ForumPostForm, ForumQuestionForm, UpdateProfile, CommentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'computingcomms/home.html', {})

def about(request):
    return render(request, 'computingcomms/about_us.html', {})

def quizzes(request):
    return render(request, 'computingcomms/quizzes.html', {})

def jp2(request):
    return render(request, 'computingcomms/jp2.html', {})

def oose2(request):
    return render(request, 'computingcomms/oose2.html', {})

def wad2(request):
    return render(request, 'computingcomms/wad2.html', {})

def ads2(request):
    return render(request, 'computingcomms/ads2.html', {})

def cs2t(request):
    return render(request, 'computingcomms/cs2t.html', {})

def af2(request):
    return render(request, 'computingcomms/af2.html', {})

def forum(request):
    posts_list = ForumPost.objects.order_by('-date')
    comments_list = Comment.objects.order_by('-date')
    context_dict = {'posts': posts_list, 'comments': comments_list}
    return render(request, 'computingcomms/forum.html', context_dict)

def add_question(request):
    registered = False

    forumQ_form = ForumQuestionForm()

    if request.method == 'POST':
        forumQ_form = ForumQuestionForm(data=request.POST)
        
        if forumQ_form.is_valid():

            user = request.user
            question = forumQ_form.save(commit=False)
            question.user = user
            question.save()
            # redirect if the thing succeeded.
            return render(request, 'computingcomms/forum.html', {'forumQ_form': forumQ_form, 'registered': registered,})
    
    return render(request, 'computingcomms/add_question.html', {'forumQ_form': forumQ_form, 'registered': registered,})


def add_image(request):
    registered = False
    forum_form = ForumPostForm()

    if request.method == 'POST':

        forum_form = ForumPostForm(request.POST)

        if forum_form.is_valid():
            user = request.user
            post = forum_form.save(commit=False)
            post.user = user
            if 'picture' in request.FILES:
                post.picture = request.FILES['picture']
            else:
                print("User has not submitted a picture")
            post.save()
            return render(request, 'computingcomms/forum.html', {'forum_form': forum_form, 'registered': registered,})
        else:
            print(forum_form.errors)
   
    return render(request, 'computingcomms/add_image.html', {'forum_form': forum_form, 'registered': registered,})

def add_comment(request):
    registered = False
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        question = request.POST.get('question')
        print (comment_form.is_valid())

        if comment_form.is_valid():

            user = request.user
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.post_id = question
            comment.save()
            # redirect if the thing succeeded.
            return render(request, 'computingcomms/forum.html', {'comment_form': comment_form, 'registered': registered,})
    
    return render(request, 'computingcomms/add_comment.html', {'comment_form': comment_form, 'registered': registered,})

   

def contact(request):
     return render(request, 'computingcomms/contact_us.html', {})

def faq(request):
    return render(request, 'computingcomms/faq.html', {})

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Computing Comms account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'computingcomms/login.html', {})

def my_account(request):
    return render(request, 'computingcomms/my_account.html', {})

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def edit_account(request):

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('edit_account'))
            
    else:
        form = UpdateProfile(instance=request.user)

    return render(request, 'computingcomms/edit_account.html',{'form' : form})
    

def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'computingcomms/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def my_questions(request):
    posts_list = ForumPost.objects.order_by('-date')
    context_dict = {'posts': posts_list,}
    return render(request, 'computingcomms/my_questions.html', context_dict)

def my_comments(request):
    posts_list = ForumPost.objects.order_by('-date')
    comments_list = Comment.objects.order_by('-date')
    context_dict = {'posts': posts_list,}
    return render(request, 'computingcomms/my_comments.html', context_dict)

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

