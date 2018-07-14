from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# ==========================列表循环数据=============================================
USER_LIST = [{"username": "Alex", "email": "125654@163.com", "gender": "男"}]
for item in range(10):
    temp = {"username": "Alex" + str(item), "email": "125654@163.com", "gender": "男"}
    USER_LIST.append(temp)

# ==========================字典循环数据=============================================
GOODS_INFO = {
    "1": {"price_in": 10, "price_out": 15},
    "2": {"price_in": 11, "price_out": 16},
    "3": {"price_in": 12, "price_out": 17},
    "4": {"price_in": 13, "price_out": 18},
    "5": {"price_in": 14, "price_out": 19},
}


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


def home(request):
    if request.method == "GET":
        return render(request, "home.html", {"user_list": USER_LIST,
                                             "goods_info": GOODS_INFO
                                             })
    else:
        # 获取数据
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        gender = request.POST.get("gender", None)
        add = {"username": username, "email": email, "gender": gender}
        USER_LIST.append(add)
        return render(request, "home.html", {"user_list": USER_LIST,
                                             "goods_info": GOODS_INFO
                                             })


def goods_index(request):
    if request.method == "GET":
        return render(request, "goods_index.html", {"goods_info": GOODS_INFO})


def goods_detail(request, nid):
    # if request.method == "GET":
    #     print(nid)
    #     return HttpResponse(GOODS_INFO[nid])
    return HttpResponse(nid)










# CBV
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