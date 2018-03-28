# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from computingcomms.models import ForumPost, UserProfile, Comment, JP2Score, WAD2Score, CS2TScore, OOSE2Score, ADS2Score, AF2Score
from computingcomms.forms import UserForm, UserProfileForm, ForumPostForm, ForumQuestionForm, UpdateProfile, CommentForm
from computingcomms.forms import JP2ScoreForm, WAD2ScoreForm, CS2TScoreForm, OOSE2ScoreForm, ADS2ScoreForm, AF2ScoreForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from collections import OrderedDict


# Create your views here.
def home(request):
    return render(request, 'computingcomms/home.html', {})

def about(request):
    return render(request, 'computingcomms/about_us.html', {})

def quizzes(request):
    return render(request, 'computingcomms/quizzes.html', {})

def jp2(request):
    # retrieves the score from the jp2 quiz and saves it to the corresponding user in the admin.py
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
    # retrieves the score from the oose2 quiz and saves it to the corresponding user in the admin.py
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
    # retrieves the score from the wad2 quiz and saves it to the corresponding user in the admin.py
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
    # retrieves the score from the ads2 quiz and saves it to the corresponding user in the admin.py
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
    # retrieves the score from the cs2t quiz and saves it to the corresponding user in the admin.py
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
    # retrieves the score from the af2 quiz and saves it to the corresponding user in the admin.py
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
            try:
                question.save()
                # redirect if the thing succeeded.
                return HttpResponseRedirect(reverse('forum'))
            except:
                return HttpResponse("Error, something went wrong :(")
    
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
            return HttpResponseRedirect(reverse('forum'))
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
            return HttpResponseRedirect(reverse('forum'))
    
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
    #retrieves each score from database
    
    context_dict = {}

    #filters each score by user for jp2
    jp2Scores = JP2Score.objects.filter(user=request.user)

    #finds the highest jp2 score, if not done the quiz then sets it to 0
    if jp2Scores.exists():
        maxjp2Score = jp2Scores.aggregate(Max('jp2score'))
        maxjp2Score = maxjp2Score['jp2score__max']
    else:
        maxjp2Score = 0

    #filters each score by user for wad2
    wad2Scores = WAD2Score.objects.filter(user=request.user)

    #finds the highest wad2score, otherwise 0 etc..
    if wad2Scores.exists():
        maxwad2Score = wad2Scores.aggregate(Max('wad2score'))
        maxwad2Score = maxwad2Score['wad2score__max']
    else:
        maxwad2Score = 0
    
    oose2Scores = OOSE2Score.objects.filter(user=request.user)

    if oose2Scores.exists():
        maxoose2Score = oose2Scores.aggregate(Max('oose2score'))
        maxoose2Score = maxoose2Score['oose2score__max']
    else:
        maxoose2Score = 0
        
    af2Scores = AF2Score.objects.filter(user=request.user)

    if af2Scores.exists():
        maxaf2Score = af2Scores.aggregate(Max('af2score'))
        maxaf2Score = maxaf2Score['af2score__max']
    else:
        maxaf2Score = 0
        
    ads2Scores = ADS2Score.objects.filter(user=request.user)

    if ads2Scores.exists():
        maxads2Score = ads2Scores.aggregate(Max('ads2score'))
        maxads2Score = maxads2Score['ads2score__max']
    else:
        maxads2Score = 0
        
    cs2tScores = CS2TScore.objects.filter(user=request.user)

    if cs2tScores.exists():
        maxcs2tScore = cs2tScores.aggregate(Max('cs2tscore'))
        maxcs2tScore = maxcs2tScore['cs2tscore__max']
    else:
        maxcs2tScore = 0

    #stores the results in a dictionary, uses an ordered dictionary to store it
    scores_dict = {'JP2 Score': maxjp2Score, 'WAD2 Score': maxwad2Score, 'OOSE2 Score': maxoose2Score, 'AF2 Score': maxaf2Score, 'ADS2 Score': maxads2Score, 'CS2T Score' : maxcs2tScore}
    od = OrderedDict(sorted(scores_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
    
    return render(request, 'computingcomms/my_account.html', {'data':od})

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
    context_dict = {'posts': posts_list, 'comments': comments_list}
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

