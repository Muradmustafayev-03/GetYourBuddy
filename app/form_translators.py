from .forms import *


def translate_reg_form(lang, request=None):
    if lang == 'en':
        return EnRegisterForm(request)
    elif lang == 'ru':
        return RuRegisterForm(request)
    return EnRegisterForm(request)


def translate_login_form(lang, request=None):
    if lang == 'en':
        return EnLoginForm(data=request)
    elif lang == 'ru':
        return RuLoginForm(data=request)
    return EnLoginForm(data=request)
