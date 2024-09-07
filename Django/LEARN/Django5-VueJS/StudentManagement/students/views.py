from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, JsonResponse
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


class StudentDeleteView(DeleteView):
    model = Student
    # form_class = StudentForm
    success_url = reverse_lazy('students_list')

    # 重写父类 delete() 方法
    def delete(self, request, *args, **kwargs):
        # 获取要删除的对象数据
        self.object = self.get_object()
        try:
            self.object.delete()
            return JsonResponse({
                'status': 'success',
                'messages': '删除成功',
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'messages': '删除失败:' + str(e)
            }, status=500)


class StudentBulkDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students_list')

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('student_ids')
        if not selected_ids:
            return JsonResponse({
                'status': 'error',
                'messages': '请选择要删除的学生信息'
            }, status=400)
        # self.get_queryset() 是从 视图类（通常是 Django 的类视图，如 ListView 或 DetailView）中获取的查询集。它调用视图中的 get_queryset() 方法，通常用于获取视图中默认使用的查询集。
        # 这是面向对象编程的方式，依赖于类视图的上下文。如果你在类视图中重写了 get_queryset() 方法，你可以灵活地改变查询集的来源。
        # 适合在类视图中使用，因为类视图通常可以处理通用查询，而 get_queryset() 提供了灵活性。
        self.object_list = self.get_queryset().filter(id__in=selected_ids)
        # Student.objects.filter() 是直接使用 Django 的模型管理器 objects，它会从数据库中直接查询 Student 模型，返回所有符合条件的记录。
        # 这是直接从模型进行查询，与类视图的上下文无关，通常适用于函数视图或者你不需要动态改变查询集的情况下。
        # selected_students = Student.objects.filter(id__in=selected_ids)
        try:
            # 删除该视图所处理的查询集中的所有对象
            self.object_list.delete()
            return JsonResponse({
                'status': 'success',
                'messages': '删除成功'
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'messages': '删除失败' + str(e)
            }, status=500)
