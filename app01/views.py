from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "login.html")

    else:
        # 获取用户名、密码
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 用户验证
        if username == "tantao258" and password == "910806":
            # return HttpResponse("登陆成功")
            # return redirect("http://www.baidu.com")     # 跳转网址
            return render(request, "home.html")           # 跳转模板
        else:
            # render 可以向html中的"error_msg"进行替换
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


def home(request):

    USER_LIST = [{"username": "Alex", "email": "125654@163.com", "gender": "男"}]
    for item in range(20):
        temp = {"username": "Alex" + str(item), "email": "125654@163.com", "gender": "男"}
        USER_LIST.append(temp)

    return render(request, "home.html", {"user_list": USER_LIST})

