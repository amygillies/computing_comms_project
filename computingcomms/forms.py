from django import forms
from django.contrib.auth.models import User
from computingcomms.models import UserProfile
from computingcomms.models import ForumPost
from computingcomms.models import Comment
from computingcomms.models import JP2Score, WAD2Score, AF2Score, OOSE2Score, ADS2Score, CS2TScore
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

class JP2ScoreForm(forms.ModelForm):
    class Meta:
        model = JP2Score
        fields = ('jp2score',)

class WAD2ScoreForm(forms.ModelForm):
    class Meta:
        model = WAD2Score
        fields = ('wad2score',)

class CS2TScoreForm(forms.ModelForm):
    class Meta:
        model = CS2TScore
        fields = ('cs2tscore',)

class OOSE2ScoreForm(forms.ModelForm):
    class Meta:
        model = OOSE2Score
        fields = ('oose2score',)

class ADS2ScoreForm(forms.ModelForm):
    class Meta:
        model = ADS2Score
        fields = ('ads2score',)

class AF2ScoreForm(forms.ModelForm):
    class Meta:
        model = AF2Score
        fields = ('af2score',)

