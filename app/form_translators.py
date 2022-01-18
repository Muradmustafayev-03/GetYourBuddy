from .forms import *


def translate_reg_form(lang, request=None):
    if lang == 'en':
        return EnRegisterForm(request)
    elif lang == 'ru':
        return RuRegisterForm(request)
    return EnRegisterForm(request)