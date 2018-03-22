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
    url(r'^my_account/', views.my_account, name='my_account'),
    url(r'^my_questions/', views.my_questions, name='my_questions'),
    url(r'^my_comments/', views.my_comments, name='my_comments'),
    url(r'^faq.', views.faq, name='faq'),
    url(r'^forum/$', views.forum, name='forum'),
    url(r'^add_question', views.add_question, name='add_question'),
    url(r'^add_image/$', views.add_image, name='add_image'),
    url(r'^add_comment', views.add_comment, name='add_comment'),
    url(r'^register', views.register, name='register'),
    url(r'^sign_out', views.sign_out, name='sign_out'),
    url(r'^edit_account/', views.edit_account, name='edit_account'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^forum/(?P<post_slug>[\w\-]+)/$', views.show_post, name='show_post')
]
