from django.shortcuts import render, HttpResponse, redirect
from app05_mysql import models


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    else:
        # 获取用户名、密码
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 用户验证
        if username == "tantao258" and password == "910806":
            # return HttpResponse("登陆成功")
            return redirect("/app01/home")     # 跳转网址

        else:
            # render 可以向html中的"error_msg"进行替换
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


def admin(request):
    if request.method == "GET":
        return render(request, "admin.html")

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        operation = request.POST.get("add", None)

        # 向数据库增加用户名、密码数据
        if operation == "增加":
            models.UserInfo.objects.create(username=username, password=password)
            return HttpResponse("添加成功")

        elif operation == "查询":
            pass

        elif operation == "删除":
            pass

        elif operation == "修改":
            pass

