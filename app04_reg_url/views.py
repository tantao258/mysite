from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
"""
1. url的正则表达式
2. 模板语言 字典的循环
"""

GOODS_INFO = {
    "1": {"price_in": 10, "price_out": 15},
    "2": {"price_in": 11, "price_out": 16},
    "3": {"price_in": 12, "price_out": 17},
    "4": {"price_in": 13, "price_out": 18},
    "5": {"price_in": 14, "price_out": 19},
}


def goods_index(request):
    if request.method == "GET":
        return render(request, "goods_index.html", {"goods_info": GOODS_INFO})


def goods_detail(request, nid):
    if request.method == "GET":
        return render(request, "goods_detail.html", {"goods_detail": GOODS_INFO[nid]})