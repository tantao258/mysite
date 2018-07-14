from django.shortcuts import render, HttpResponse, redirect
import os
# Create your views here.
# 获取前端数据的方式

def questionnaire(request):
    if request.method == "GET":
        return render(request, "questionnaire.html")

    elif request.method == "POST":
        # 获取前端数据
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        gender = request.POST.get("gender", None)
        hobby = request.POST.getlist("hobby", None)
        city = request.POST.get("city", None)
        area = request.POST.get("area", None)

        # 上传文件  form 标签中设置：enctype="multipart/form-data"
        file = request.FILES.get("filename")   # file 是一个对象
        # print(file, type(file), file.name)
        with open(os.path.join("upload", file.name), mode="wb") as f:
            for i in file.chunks():
                f.write(i)

        return HttpResponse("提交成功，谢谢您的配合。")

    else:
        return render(request, "questionnaire.html")