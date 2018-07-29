from django.shortcuts import render, HttpResponse, redirect
from novel_search import models
from utils.page import page
# Create your views here.


def novel_index(request):
    if request.method == "GET":
        operation = request.GET.get("operation", None)
        if operation == "search":
            search_content = request.GET.get("search_content", None)
            return HttpResponse(search_content)

        elif operation is None:
            books = models.NovelInfo.objects.order_by("-click_times")

        current_page = 1
        next_page_info = page(items=books, current_page=current_page, num_one_page=10)
        return render(request, "novel-search.html", {"next_page_info": next_page_info})


def novel_sorted(request, nid, uid, page_id):
    print(nid, uid, page_id)

    # get sort_condition
    if nid == "1":
        sort_condition = "read_times"
    elif nid == "2":
        sort_condition = "review_times"
    elif nid == "3":
        sort_condition = "collection_times"
    elif nid == "4":
        sort_condition = "click_times"
    elif nid == "5":
        sort_condition = "popularity"

    # get sort_direction
    if uid == "1":                     # 降序
        sort_direction = "-"
    elif uid == "0":
        sort_direction = ""            # 升序

    books = models.NovelInfo.objects.order_by(sort_direction + sort_condition)

    current_page = int(page_id)

    next_page_info = page(items=books, current_page=current_page, num_one_page=10)
    return render(request, "novel-search.html", {"next_page_info": next_page_info})


