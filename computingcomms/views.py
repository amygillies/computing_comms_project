# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from computingcomms.models import ForumPost, UserProfile, Comment
from computingcomms.forms import UserForm, UserProfileForm, ForumPostForm, ForumQuestionForm, UpdateProfile, CommentForm
from computingcomms.forms import JP2ScoreForm, WAD2ScoreForm, CS2TScoreForm, OOSE2ScoreForm, ADS2ScoreForm, AF2ScoreForm
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
    registered = False
    if request.method == 'POST':
        jp2_score_form = JP2ScoreForm(data=request.POST)

        if jp2_score_form.is_valid():
            user = request.user
            jp2score = jp2_score_form.save(commit=False)
            jp2score.user = user
            jp2score.save()
    else:
        jp2_score_form = JP2ScoreForm()
    return render(request, 'computingcomms/jp2.html', {'jp2_score_form': jp2_score_form, 'registered': registered,})

def oose2(request):
    registered = False
    if request.method == 'POST':
        oose2_score_form = OOSE2ScoreForm(data=request.POST)

        if oose2_score_form.is_valid():
            user = request.user
            oose2score = oose2_score_form.save(commit=False)
            oose2score.user = user
            oose2score.save()
    else:
        oose2_score_form = OOSE2ScoreForm()
    return render(request, 'computingcomms/oose2.html', {'oose2_score_form': oose2_score_form, 'registered': registered,})

def wad2(request):
    registered = False
    if request.method == 'POST':
        wad2_score_form = WAD2ScoreForm(data=request.POST)

        if wad2_score_form.is_valid():
            user = request.user
            wad2score = wad2_score_form.save(commit=False)
            wad2score.user = user
            wad2score.save()
    else:
        wad2_score_form = WAD2ScoreForm()
    return render(request, 'computingcomms/wad2.html', {'wad2_score_form': wad2_score_form, 'registered': registered,})

def ads2(request):
    registered = False
    if request.method == 'POST':
        ads2_score_form = ADS2ScoreForm(data=request.POST)

        if ads2_score_form.is_valid():
            user = request.user
            ads2score = ads2_score_form.save(commit=False)
            ads2score.user = user
            ads2score.save()
    else:
        ads2_score_form = ADS2ScoreForm()
    return render(request, 'computingcomms/ads2.html', {'ads2_score_form': ads2_score_form, 'registered': registered,})

def cs2t(request):
    registered = False
    if request.method == 'POST':
        cs2t_score_form = CS2TScoreForm(data=request.POST)

        if cs2t_score_form.is_valid():
            user = request.user
            cs2tscore = cs2t_score_form.save(commit=False)
            cs2tscore.user = user
            cs2tscore.save()
    else:
        cs2t_score_form = CS2TScoreForm()
    return render(request, 'computingcomms/cs2t.html', {'cs2t_score_form': cs2t_score_form, 'registered': registered,})

def af2(request):
    registered = False
    if request.method == 'POST':
        af2_score_form = AF2ScoreForm(data=request.POST)

        if af2_score_form.is_valid():
            user = request.user
            af2score = af2_score_form.save(commit=False)
            af2score.user = user
            af2score.save()
    else:
        af2_score_form = AF2ScoreForm()
    return render(request, 'computingcomms/af2.html', {'af2_score_form': af2_score_form, 'registered': registered,})

def forum(request):
    posts_list = ForumPost.objects.order_by('-date')
    comments_list = Comment.objects.order_by('-date')[:3]
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

def add_comment(request,post_slug):
    print("adding comment")
    registered = False
    try:
        post = ForumPost.objects.get(slug=post_slug)
    except:
        print("failed")
        post = None
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            user = request.user
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.post = post
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

def show_post(request, post_slug):
    context_dict = {}

    try:
        post = ForumPost.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post = post).order_by('-date')
        context_dict['post'] = post
        context_dict['comments'] = comments
    except:
        context_dict['post'] = None
        context_dict['comments'] = None

    return render(request,'computingcomms/post.html' ,context_dict)

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

