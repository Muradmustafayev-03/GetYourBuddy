from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from .form_translators import *


def welcome(request, lang='en'):
    if lang == 'en':
        return render(request, "en/welcome.html", {})
    elif lang == 'ru':
        return render(request, "ru/welcome.html", {})


def login_page(request, lang='en'):
    if lang == 'en':
        return render(request, "en/login.html", {})
    elif lang == 'ru':
        return render(request, "ru/login.html", {})


def registration(request, lang='en'):
    error = ''
    if request.method == "POST":
        form = translate_reg_form(lang, request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username} has successfully registered")
            user_profile = Profile.objects.filter(username=user.username)[0]
            return profile(request, user_profile, lang)
        error = form.errors
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = translate_reg_form(lang)

    if lang == 'en':
        return render(request, "en/registration.html", {'form': form, 'error': error})
    elif lang == 'ru':
        return render(request, "ru/registration.html", {'form': form})


def profile(request, user, lang='en'):
    return render(request, f"{lang}/profile.html", {'nickname': user.nickname,
                                                    'photo': user.photo,
                                                    'birthdate': user.birthdate,
                                                    'country': user.country,
                                                    'city': user.city,
                                                    'bio': user.bio})
