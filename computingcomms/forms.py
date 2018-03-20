from django import forms
from django.contrib.auth.models import User
from computingcomms.models import UserProfile
from computingcomms.models import ForumPost


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

class ForumQuestionForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('question',)

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user
