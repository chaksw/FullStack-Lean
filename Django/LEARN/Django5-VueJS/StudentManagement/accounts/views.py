from django.shortcuts import render
from django.http import JsonResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from teachers.models import Teacher
from students.models import Student

# Create your views here.


def user_login(request):
    # 判断是否为 post 请求
    if request.method == 'POST':
        # form 表单验证
        # 传入 POST 请求数据，建立对应表单对象
        form = LoginForm(request.POST)
        # 验证失败
        if not form.is_valid():
            return JsonResponse({'status': 'error', 'messages': '提交信息有误！'}, status=400, safe=False)
        # 验证成功
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        role = form.cleaned_data.get('role')
        # 判断角色
        if role == 'teacher':
            try:
                teacher = Teacher.objects.get(phone_number=username)
                user_name = teacher.teacher_name + '_' + teacher.phone_number
                # Django 自带的用户验证方法
                user = authenticate(username=user_name, password=password)
                # users = User.objects.filter(username=teacher.user.username)
                # authenticate(username=teacher.user.username, password=password)
            except Teacher.DoesNotExist:
                return JsonResponse({'status': 'error', 'messages': '老师信息不存在'}, status=404)
        elif role == 'student':
            try:
                student = Student.objects.get(student_number=username)
                user_name = student.student_name + '_' + student.student_number
                # Django 自带的用户验证方法
                user = authenticate(username=user_name, password=password)
            except Student.DoesNotExist:
                return JsonResponse({'status': 'error', 'messages': '学生信息不存在'}, status=404)
        elif role == 'admin':
            try:
                user = authenticate(username=username, password=password)
            except User.DoesNotExist:
                print('asdasdasd')
                return JsonResponse({'status': 'error', 'messages': '管理员信息不存在'}, status=404)

        # 验证成功，返回 json 数据
        if user is not None:
            if user.is_active:
                # 把登录信息等常用信息写入session会话
                # Session 会话在 Django 中的作用是在用户和服务器之间保存临时数据，从而在多个请求之间维持用户的状态。通常，HTTP 是一种无状态的协议，每个请求之间没有关联，而 Session 机制使得我们能够在请求间保持用户的状态。

                # 主要作用：
                # 维持用户登录状态：
                # Session 用于跟踪用户登录信息。在用户登录之后，Django 会将用户的登录状态保存在会话中，用户不需要在每个请求中重新登录。

                # 保存临时数据：
                # 可以使用 Session 存储一些用户特定的临时数据。例如，在一个购物车应用中，用户添加到购物车中的商品数据可以保存在会话中。

                # 跨请求共享数据：
                # Django Session 允许你在多个请求之间保存和访问数据。例如，用户在表单中输入的一些数据，可以在会话中保留，以便在提交失败后保留用户输入的信息。
                # login() 会将 user 对象的信息写入 session 中
                login(request=request, user=user)

                # 将 role 写入 session，后续根据 role 来展示页面和提供功能
                request.session['user_role'] = role
                return JsonResponse({'status': 'success', 'messages': '登录成功', 'role': role})
            else:
                return JsonResponse({'status': 'error', 'messages': '账户已被禁用'}, status=403)
        else:
            return JsonResponse({'status': 'error', 'messages': '用户名或密码错误'}, status=401)

    return render(request, 'accounts/login.html')
