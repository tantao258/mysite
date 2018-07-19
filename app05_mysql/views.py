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

        if request.POST.get("add", None) == "增加":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            user_group_id = 2
            cobj_id = 4
            uobj_id =10

            # models.UserInfo.objects.create(username=username, password=password, user_group_id=user_group_id)
            models.UserToCustomer.objects.create(cobj_id=cobj_id, uobj_id=uobj_id)
            return HttpResponse("添加成功")

        elif request.POST.get("query", None) == "查询":
            """
                # obj_list = models.UserInfo.objects.all()    # 查询全部
                # 查询全部并只取指定字段用value，返回嵌套字典的列表，跨表用 "__"
                # obj_list = models.UserInfo.objects.all().values("username", "password")
                # obj_list = models.UserInfo.objects.filter(username="tantao258", password=9108077776)
                # 返回querySet类型[对象object 的列表]
                # result = [object(ID, username, password), object(ID, username, password)]
            """
            """
            obj_list = models.UserInfo.objects.filter(username="tantao258")  # 条件查询
            print(obj_list)
            for item in obj_list:
                print(item.id)
                print(item.username)
                print(item.password)
                print(item.user_group_id)
                print(item.user_group)
                print(item.user_group.uid)
                print(item.user_group.group)
            """
            obj_list = models.UserToCustomer.objects.filter(cobj_id=4)
            for obj in obj_list:
                # print(obj.cobj_id, obj.uobj_id, obj.cobj, obj.uobj)
                # print(obj.cobj.id)
                # print(obj.cobj.name)
                # print("------------------")
                # print(obj.uobj.id)
                # print(obj.uobj.username)
                # print(obj.uobj.password)
                # print(obj.uobj.user_group_id)
                # print(obj.uobj.user_group)
                print(print(obj.uobj.user_group.group))
                print("==========================================")

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




