from django.shortcuts import render, HttpResponse, redirect
from background import models
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "admin.html")

    elif request.method == "POST":
        # 获取后台用户名密码
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        result = models.UserInfo.objects.filter(username=username, password=password)
        # 登陆成功
        if len(result) != 0:
            return redirect("/background/admin-detail.html")
        # 登录失败
        else:
            return render(request, "admin.html", {"error_msg": "用户名或密码错误！"})

def detail(request):
    # 显示所有用户
    all_users = models.UserInfo.objects.all()

    if request.method == "GET":
        return render(request, "admin-detail.html", {"all_users": all_users})
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        telephone = request.POST.get("telephone", None)
        operation = request.POST.get("operation", None)

        if operation == "增加":
            models.UserInfo.objects.create(username=username, password=password, email=email, telephone=telephone)
            return render(request, "admin-detail.html", {"all_users": all_users, "msg": "添加成功"})
        elif operation == "删除":
            models.UserInfo.objects.filter(username=username).delete()
            return render(request, "admin-detail.html", {"all_users": all_users, "msg": "删除成功"})
        elif operation == "更新":
            if len(password) != 0:
                models.UserInfo.objects.filter(username=username).update(password=password)
            if len(email) != 0:
                models.UserInfo.objects.filter(username=username).update(email=email)
            if len(telephone) != 0:
                models.UserInfo.objects.filter(username=username).update(telephone=telephone)
            return render(request, "admin-detail.html", {"all_users": all_users, "msg": "更新成功"})
        elif operation == "筛选":
            filter_users = models.UserInfo.objects.filter(username=username)
            return render(request, "admin-detail.html", {"all_users": all_users, "filter_users": filter_users})

