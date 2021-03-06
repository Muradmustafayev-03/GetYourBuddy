from django import forms
from django_countries import countries
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from app.models import *

# Create your forms here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2', 'email', 'nickname',
                  'photo', 'birthdate', 'country', 'city', 'bio')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EnRegisterForm(RegisterForm):
    username = forms.CharField(label='Create a username:',
                               widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                             'placeholder': 'Username'}))
    password1 = forms.CharField(label='Create a password:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm your password:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))

    email = forms.EmailField(label='Enter your email address:', required=False,
                             widget=forms.EmailInput(attrs={'class': 'login_form_input',
                                                            'placeholder': 'someone@mail.com'}))

    photo = forms.ImageField(label='Upload a profile photo', required=False,
                             widget=forms.FileInput(attrs={'class': 'image_input'}))
    nickname = forms.CharField(label='Enter your name or nickname:', required=True,
                               widget=forms.TextInput(attrs={'class': 'login_form_input'}))

    birthdate = forms.DateField(label='Enter your date of birth:', required=False,
                                widget=forms.DateInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Select a date',
                                    'type': 'date'}))
    country = forms.ChoiceField(choices=(("", "-"),) + tuple(countries), label='Country:', required=False)
    city = forms.CharField(label='City/Town', required=False,
                           widget=forms.TextInput(attrs={'class': 'login_form_input'}))
    bio = forms.CharField(label='Write something about yourself:', required=False,
                          widget=forms.Textarea())


class RuRegisterForm(RegisterForm):
    username = forms.CharField(label='???????????????????? ??????????:',
                               widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                             'placeholder': '??????????'}))
    password1 = forms.CharField(label='???????????????????? ????????????:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(label='?????????????????????? ????????????:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))

    email = forms.EmailField(label='?????????????? ?????? email:', required=False,
                             widget=forms.EmailInput(attrs={'class': 'login_form_input',
                                                            'placeholder': 'someone@mail.com'}))

    photo = forms.ImageField(label='?????????????????? ????????????????????', required=False,
                             widget=forms.FileInput(attrs={'class': 'image_input'}))
    nickname = forms.CharField(label='???????????????????? ??????????????', required=True,
                               widget=forms.TextInput(attrs={'class': 'login_form_input'}))

    birthdate = forms.DateField(label='?????????????? ???????? ????????????????', required=False,
                                widget=forms.DateInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Select a date',
                                    'type': 'date'}))
    country = forms.ChoiceField(choices=(("1", "-"),) + tuple(countries), label='????????????')
    city = forms.CharField(label='??????????', required=False,
                           widget=forms.TextInput(attrs={'class': 'login_form_input'}))
    bio = forms.CharField(label='???????????????? ??????-???????????? ?? ????????', required=False,
                          widget=forms.Textarea())


class EnLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter your username:',
                               widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                             'placeholder': 'Username'}))

    password = forms.CharField(label='Enter your password:',
                               strip=False,
                               widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                 'class': 'login_form_input',
                                                                 'placeholder': 'Password'}))


class RuLoginForm(AuthenticationForm):
    username = forms.CharField(label='?????????????? ?????? ??????????:',
                               widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                             'placeholder': '??????????'}))

    password = forms.CharField(label='?????????????? ?????? ????????????:',
                               strip=False,
                               widget=forms.PasswordInput(attrs={'autocomplete': 'password',
                                                                 'class': 'login_form_input',
                                                                 'placeholder': 'Password'}))
