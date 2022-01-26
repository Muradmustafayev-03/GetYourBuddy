from django import forms
from django_countries import countries
from django.contrib.auth.forms import UserCreationForm
from app.models import *

COUNTRIES = (("1", "-"),) + tuple(countries)


# Create your forms here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2', 'nickname', 'photo', 'birthdate', 'country', 'city', 'bio')

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
    country = forms.ChoiceField(choices=COUNTRIES, label='Country:')
    city = forms.CharField(label='City/Town', required=False,
                           widget=forms.TextInput(attrs={'class': 'login_form_input'}))
    bio = forms.CharField(label='Write something about yourself:', required=False,
                          widget=forms.Textarea())


class RuRegisterForm(RegisterForm):
    username = forms.CharField(label='Придумайте логин:',
                               widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                             'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Придумайте пароль:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(label='Подтвердите пароль:',
                                strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'login_form_input',
                                                                  'placeholder': 'Password'}))

    email = forms.EmailField(label='Введите ваш email:', required=False,
                             widget=forms.EmailInput(attrs={'class': 'login_form_input',
                                                            'placeholder': 'someone@mail.com'}))

    photo = forms.ImageField(label='Загрузите фотографию', required=False,
                             widget=forms.FileInput(attrs={'class': 'image_input'}))
    nickname = forms.CharField(label='Придумайте никнейм', required=True,
                               widget=forms.TextInput(attrs={'class': 'login_form_input'}))

    birthdate = forms.DateField(label='Введите дату рождения', required=False,
                                widget=forms.DateInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Select a date',
                                    'type': 'date'}))
    country = forms.ChoiceField(choices=COUNTRIES, label='Страна')
    city = forms.CharField(label='Город', required=False,
                           widget=forms.TextInput(attrs={'class': 'login_form_input'}))
    bio = forms.CharField(label='Напишите что-нибудь о себе', required=False,
                          widget=forms.Textarea())
