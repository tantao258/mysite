from django.shortcuts import render, HttpResponse, redirect
from novel_search import models
from utils.page import page
# Create your views here.


def novel_index(request):
    if request.method == "GET":
        operation = request.GET.get("operation", None)
        if operation == "sort":
            filter = request.GET.get("filter", None)
            sort_direction = request.GET.get("sort_direction", None)
            if filter is not None:
                if sort_direction == "0":
                    books = models.NovelInfo.objects.order_by(filter)
                elif sort_direction == "1":
                    books = models.NovelInfo.objects.order_by("-" + filter)

        elif operation == "search":
            search_content = request.GET.get("search_content", None)
            return HttpResponse(search_content)

        elif operation is None:
            books = models.NovelInfo.objects.all()

        current_page = 1
        next_page_info = page(items=books, current_page=current_page, num_one_page=10)
        return render(request, "novel-search.html", {"next_page_info": next_page_info})


def novel_sorted(request, nid, uid, pid):

    print(nid, uid, pid)
    return HttpResponse("sorted")
