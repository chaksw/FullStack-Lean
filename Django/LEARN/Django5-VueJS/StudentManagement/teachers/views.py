from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Teacher
from grades.models import Grade
from .forms import TeacherForm
# Create your views here.


class BaseTeacherView():
    model = Teacher
    success_url = reverse_lazy('teachers_list')


class TeacherListView(BaseTeacherView, ListView):
    # 1.基础定义：指定显示的前端页面，以及定义上下文变量
    template_name = "teachers/teachers_list.html"
    # context_object_name 用于指定传递给模板的上下文变量的名称。
    context_object_name = 'teachers'
    # 2.分页，显示特定数量的数据
    paginate_by = 10

    # 3.搜索功能：基于特定字段过滤数据
    def get_context_data(self):
        context = super().get_context_data()
        context['grades'] = Grade.objects.all().order_by('grade_number')
        context['current_grade'] = self.request.GET.get('grade', '')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('search')
        grade_id = self.request.GET.get('grade')
        if grade_id:
            queryset = queryset.filter(grade_id__icontains=grade_id)
        if keyword:
            filter = Q(teacher_name__icontains=keyword) | Q(phone_number__icontains=keyword)
            queryset = queryset.filter(filter)
        return queryset

    # 4.排序：基于特定字段的特定规则进行排序


class TeacherCreateView(BaseTeacherView, CreateView):
    # 1. 基础定义：
    template_name = "teachers/teacher_form.html"
    form_class = TeacherForm

    # 接受form表单数据并创建对应用户 （字段验证发生在这之前，在 form 的clean_<field_data>中进行
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


class TeacherDeleteView(BaseTeacherView, DeleteView):
    template_name = "teachers/teachers_list.html"


class TeacherBulkDeleteView(BaseTeacherView, DeleteView):
    pass


def upload_teacher():
    pass