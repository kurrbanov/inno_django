"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from application.views import main_page, laptops, search, registration, login_page, logout_page, top_secret

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name=''),
    path('laptops/', laptops, name='laptops'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('top_secret', top_secret, name='top_secret')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
