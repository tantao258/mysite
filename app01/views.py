from django.shortcuts import render, HttpResponse, redirect
# Create your views here.


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
            return redirect("/home")     # 跳转网址

        else:
            # render 可以向html中的"error_msg"进行替换
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


USER_LIST = [{"username": "Alex", "email": "125654@163.com", "gender": "男"}]
for item in range(20):
    temp = {"username": "Alex" + str(item), "email": "125654@163.com", "gender": "男"}
    USER_LIST.append(temp)


def home(request):
    if request.method == "GET":
        return render(request, "home.html", {"user_list": USER_LIST})
    else:
        # 获取数据
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        gender = request.POST.get("gender", None)
        add = {"username": username, "email": email, "gender": gender}
        USER_LIST.append(add)
        return render(request, "home.html", {"user_list": USER_LIST})



# CBV
from django.views import View
class Login(View):

    # 装饰器
    def dispatch(self, request, *args, **kwargs):
        # 调用父类中dispatch方法
        result = super(Login, self).dispatch(request, *args, **kwargs)
        return result

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # 获取用户名、密码
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 用户验证
        if username == "tantao258" and password == "910806":
            # return HttpResponse("登陆成功")
            return redirect("/home")  # 跳转网址

        else:
            # render 可以向html中的"error_msg"进行替换
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
