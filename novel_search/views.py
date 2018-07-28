from django.shortcuts import render, HttpResponse, redirect
from novel_search import models
from utils.page import page
# Create your views here.


def novel_search(request):
    books = models.NovelInfo.objects.all()
    current_page = 2
    next_page_info = page(items=books, current_page=2, num_one_page=10)

    return render(request, "novel-search.html", {""})
