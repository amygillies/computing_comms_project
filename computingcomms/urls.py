from django.conf.urls import url
from computingcomms import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about_us/', views.about, name='about_us'),
    url(r'^contact_us/', views.contact, name='contact_us'),
    url(r'^quizzes/', views.quizzes, name='quizzes'),
    url(r'^jp2/', views.jp2, name='jp2'),
    url(r'^oose2/', views.oose2, name='oose2'),
    url(r'^wad2/', views.wad2, name='wad2'),
    url(r'^ads2/', views.ads2, name='ads2'),
    url(r'^cs2t/', views.cs2t, name='cs2t'),
    url(r'^af2/', views.af2, name='af2'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^myaccount/', views.my_account, name='myaccount'),
    url(r'^myquestions/', views.my_questions, name='myquestions'),
    url(r'^mycomments/', views.my_comments, name='mycomments'),
    url(r'^faq.', views.faq, name='faq'),
    url(r'^forum', views.forum, name='forum'),
]
