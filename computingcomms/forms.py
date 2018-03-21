from django import forms
from django.contrib.auth.models import User
from computingcomms.models import UserProfile
from computingcomms.models import ForumPost
from computingcomms.models import Comment
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('question','picture',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class ForumQuestionForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('question',)

class UpdateProfile(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', )

