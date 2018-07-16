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
        result = models.UserInfo.objects.filter(username=username, password=password)
        if len(result) != 0:
            print(result[0].id, result[0].username, result[0].password)
            return HttpResponse("登陆成功")

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

        print()
        # 向数据库增加用户名、密码数据
        if request.POST.get("add", None) == "增加":
            models.UserInfo.objects.create(username=username, password=password)
            return HttpResponse("添加成功")

        elif request.POST.get("query", None) == "查询":

            # result = models.UserInfo.objects.all()    # 查询全部
            # 查询全部并只取指定字段用value，返回嵌套字典的列表，跨表用 "__"
            # result = models.UserInfo.objects.all().values("username", "password")
            result = models.UserInfo.objects.filter(username="tantao258")   # 条件查询
            result = models.UserInfo.objects.filter(username="tantao258", password=9108077776) # and 条件查询
            # 查询结果返回对象列表
            # print(len(result))
            # result = [object(ID, username, password), object(ID, username, password),,object(ID, username, password)]
            for item in result:
                print(item.id, item.username, item.password)
            return HttpResponse("查询成功")

        elif request.POST.get("delete", None) == "删除":
            # models.UserInfo.objects.all().delete()  # 删除数据表全部
            models.UserInfo.objects.filter(username="tantao258").delete()

            return HttpResponse("删除成功")

        elif request.POST.get("modify", None) != None:
            # 更新
            # models.UserInfo.objects.all().update(password=666666)
            models.UserInfo.objects.filter(id=1).update(password=666666)
            return HttpResponse("修改成功")


