"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import app01.views as views01
import app02.views as views02

urlpatterns = [
    path('admin/', admin.site.urls),

    # FBV --------------------------
    path('login/', views01.login),
    # CBV
    # path('login/', views01.Login.as_view()),
    path('home/', views01.home),
    path('questionnaire/', views02.questionnaire),
    path('goods_index/', views01.goods_index),
    path('goods_detail-(\d+).html', views01.goods_detail),











]
