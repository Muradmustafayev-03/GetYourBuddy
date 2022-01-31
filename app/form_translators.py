from .forms import *


def translate_reg_form(lang, post=None, files=None):
    if lang == 'en':
        return EnRegisterForm(post, files)
    elif lang == 'ru':
        return RuRegisterForm(post, files)
    return EnRegisterForm(post, files)


def translate_login_form(lang, request=None):
    if lang == 'en':
        return EnLoginForm(data=request)
    elif lang == 'ru':
        return RuLoginForm(data=request)
    return EnLoginForm(data=request)
