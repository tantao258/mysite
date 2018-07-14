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
from app04_reg_url import views

urlpatterns = [

    # -------------------------url 正则表达式-------------------
    path('goods_index/', views.goods_index, name="i1"),
    # re_path('goods_detail/(\d+).html', views04.goods_detail, name="i2"),
    re_path('goods_detail/(?P<nid>\d+).html', views.goods_detail, name="i3"),
]