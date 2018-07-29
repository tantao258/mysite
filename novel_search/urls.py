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
from django.urls import path, re_path
from novel_search import views

urlpatterns = [
        path('novel_index.html/', views.novel_index, name="novel_index"),

        re_path('novel_sort=(?P<nid>\d+)_(?P<uid>\d+)&page=(?P<page_id>\d+)/',
                views.novel_sorted,
                name="novel_sorted"),
]