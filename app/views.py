from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django_countries.data import COUNTRIES
from .form_translators import *


def welcome(request, lang='en'):
    if lang == 'en':
        return render(request, "en/welcome.html", {})
    elif lang == 'ru':
        return render(request, "ru/welcome.html", {})


def login_request(request, lang='en'):
    error = ''
    if request.method == "POST":
        form = translate_login_form(lang, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f"{user.username} has successfully logged in")
            user_profile = Profile.objects.filter(username=user.username)[0]
            return redirect(f'/{lang}/profile/{user_profile.id}')
        error = form.errors
        messages.error(request, "Unsuccessful log in attempt. Invalid information.")

    form = translate_login_form(lang)

    return render(request, f"{lang}/login.html", {'form': form, 'error': error})


def registration(request, lang='en'):
    error = ''
    if request.method == "POST":
        form = translate_reg_form(lang, request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username} has successfully registered")
            user_profile = Profile.objects.filter(username=user.username)[0]
            return redirect(f'/{lang}/profile/{user_profile.id}')
        error = form.errors
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = translate_reg_form(lang)

    return render(request, f"{lang}/registration.html", {'form': form, 'error': error})


def profile(request, user_id, lang='en'):
    user = Profile.objects.filter(id=user_id)[0]
    country = ''
    try:
        country = COUNTRIES[user.country]
    except KeyError:
        pass
    return render(request, f"{lang}/profile.html", {'user_id': user.id,
                                                    'nickname': user.nickname,
                                                    'photo': user.photo,
                                                    'birthdate': user.birthdate,
                                                    'country': country,
                                                    'city': user.city,
                                                    'bio': user.bio,
                                                    'user': user})
