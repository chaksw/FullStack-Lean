from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Teacher
from grades.models import Grade
from .forms import TeacherForm
from utils.permissions import RoleRequiredMixin
# Create your views here.


class BaseTeacherView(RoleRequiredMixin):
    model = Teacher
    success_url = reverse_lazy('teachers_list')
    allowed_roles = ['admin']


class TeacherListView(BaseTeacherView, ListView):
    # 1.基础定义：指定显示的前端页面，以及定义上下文变量
    template_name = "teachers/teachers_list.html"
    # context_object_name 用于指定传递给模板的上下文变量的名称。
    context_object_name = 'teachers'
    # 2.分页，显示特定数量的数据
    paginate_by = 10

    # 3.搜索功能：基于特定字段过滤数据

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('search')
        grade_id = self.request.GET.get('grade')
        if grade_id:
            queryset = queryset.filter(grade__pk=grade_id)
        if keyword:
            filter = Q(teacher_name__icontains=keyword) | Q(phone_number__icontains=keyword)
            queryset = queryset.filter(filter)
        return queryset

    # 定义班级下拉栏的排序方式，并将当前被选班级加入到上下文 context 中
    def get_context_data(self):
        context = super().get_context_data()
        context['grades'] = Grade.objects.all().order_by('grade_number')
        context['current_grade'] = self.request.GET.get('grade', '')
        return context

    # 4.排序：基于特定字段的特定规则进行排序


class TeacherCreateView(BaseTeacherView, CreateView):
    # 1. 基础定义：
    template_name = "teachers/teacher_form.html"
    form_class = TeacherForm

    # 接受form表单数据并创建对应用户 （字段验证发生在这之前，在 form 的clean_<field_data>中进行）
    def form_valid(self, form):
        # 接受字段
        teacher_name = form.cleaned_data.get('teacher_name')
        phone_number = form.cleaned_data.get('phone_number')
        # 创建对应用户
        username = f'{teacher_name}_{phone_number}'
        password = phone_number[-6:]
        # 确保带创建用户不存在，否则直接使用已存在的同名用户
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
        else:
            user = User.objects.create_user(username=username, password=password)
        # 将用户写入 teacher, 模型实例关联
        form.instance.user = user
        form.save()

        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    def form_invalid(self, form):
        errors = form.errors.as_json()
        print(errors)
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)


class TeacherUpdateView(BaseTeacherView, UpdateView):
    template_name = "teachers/teacher_form.html"
    form_class = TeacherForm

    def form_valid(self, form):
        teacher = form.save(commit=False)
        if 'teacher_name' in form.changed_data or 'phone_number' in form.changed_data:
            teacher_name = form.cleaned_data.get('teacher_name')
            phone_number = form.cleaned_data.get('phone_number')
            teacher.user.username = f'{teacher_name}_{phone_number}'
            teacher.user.password = make_password(phone_number[-6:])
            teacher.user.save()
        teacher.save()
        response = {
            'status': 'success',
            'messages': '操作成功'
        }
        return JsonResponse(response, status=200)

    def form_invalid(self, form):
        errors = form.errors.as_json()
        response = {
            'status': 'error',
            'messages': errors
        }
        return JsonResponse(response, status=400)


class TeacherDeleteView(BaseTeacherView, DeleteView):
    template_name = "teachers/teachers_list.html"

    def delete(self, request, *args, **kwargs):
        # self.get_object() 时，Django 会自动基于 URL 参数获取对象。Django 提供这个方法来封装对象检索的逻辑，确保代码的简洁性和一致性。
        self.object = self.get_object()
        try:
            self.object.delete()
            response = {
                'status': 'success',
                'messages': '删除成功',
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            response = {
                'status': 'error',
                'messages': '删除失败' + str(e)
            }
            return JsonResponse(response, status=500)
