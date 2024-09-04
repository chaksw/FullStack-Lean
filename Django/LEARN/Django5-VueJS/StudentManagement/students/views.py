from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'students/students_list.html'
    # fields = []
    context_object_name = 'students'

    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super().get_queryset()


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_class = 'students/student_form.html'
    # success_url = reverse_lazy('students_list')
    # 当 type='sumbit' 的按钮按下后，会提交表单，产生一个 post 请求，将表单数据发送到服务器
    # 服务器接收到数据后，CreateView 会调用 ModelForm 中的各种方法，包括 form.is_valid(), clean_<field_name> 方法来验证数据是否合法
    #
    # 如果数据有效，默认情况下 form_valid() 会被执行， 其中会自动调用 form.save() 将数据保存到数据库中，（如果重写了 form_valid()，则不会自动调用 form.save(), 而需要显示调用)
    # 如果数据保存，会重定向到 success_url 中指定的页面
    # 表单字段验证

    def form_valid(self, form):
        # 接收字段
        student_name = form.cleaned_data.get('student_name')
        student_number = form.cleaned_data.get('student_number')
        # 写入 auth_user 表，username为 student_name + student_number, 密码为 student_number 后6位
        username = f"{student_name}_{student_number}"
        password = student_number[-6:]
        users = User.objects.filter(username=username)
        if users.exists():
            # 如果已存在相同 username 的 user
            user = users.first()
        else:
            # 如果不存在，使用 django 自带的 User.objects.create_user(), 该方法会自动对密码进行加密
            user = User.objects.create_user(username=username, password=password)
        # 将用户写入 student, 模型实例关联
        form.instance.user = user
        form.save()
        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    # 重写父类方法，定义表单验证失败时的逻辑
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_class = 'students/student_form.html'

    def form_valid(self, form):
        # 获取学生对象实例, commont=False: 表示暂时不将实例保存到数据库中
        student = form.save(commit=False)
        # form.changed_data 返回一个包含表单中已更改字段名称的列表
        if 'studnet_name' in form.changed_data or 'student_number' in form.changed_data:
            # 更改 user username & password
            student_name = form.cleaned_data.get('student_name')
            student_number = form.cleaned_data.get('student_number')
            student.user.username = f"{student_name}_{student_number}"
            # 使用 make_password 对修改的密码进行加密 （create 时是使用 User.objects.create_user，这里面会调用 make_password
            student.user.password = make_password(student_number[-6:])
            student.user.save()  # 保存更改
        student.save()
        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    # 重写父类方法，定义表单验证失败时的逻辑
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)
