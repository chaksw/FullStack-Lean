from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 接受请求，通过 render 函数引入希望渲染的html文件


def login(request):
    # post 请求的业务逻辑，只有在提交表达时才会触发
    # if request.method == 'POST' 等效
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 登陆业务逻辑，验证用户 ｜ 密码是否在数据库中等，这里模拟登陆成功的逻辑
        return HttpResponse(f'login success with {username} and password {password}')
    # 默认是 GET() 请求，渲染 login.html
    return render(request, 'login.html')
