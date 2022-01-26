"""GetYourBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.welcome, name='welcome'),
    path('<str:lang>/', app.views.welcome, name='welcome'),
    path('<str:lang>/welcome/', app.views.welcome, name='welcome'),
    path('<str:lang>/login/', app.views.login_request, name='login'),
    path('<str:lang>/registration/', app.views.registration, name='registration'),
    path('<str:lang>/profile/', app.views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
