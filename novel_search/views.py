from django.shortcuts import render, HttpResponse, redirect
from novel_search import models
# Create your views here.


def novel_search(request):
    books = models.NovelInfo.objects.all()
    return render(request, "novel-search.html", {"books": books})
