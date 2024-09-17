from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Teacher
from .forms import TeacherForm
from django.urls import reverse_lazy
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

    # 4.排序：基于特定字段的特定规则进行排序


class TeacherCreateView(BaseTeacherView, CreateView):
    # 1. 基础定义：
    template_name = "teachers/teacher_form.html"
    form_class = TeacherForm


class TeacherUpdateView(BaseTeacherView, UpdateView):
    template_name = "teachers/teacher_form.html"


class TeacherDeleteView(BaseTeacherView, DeleteView):
    template_name = "teachers/teachers_list.html"


class TeacherBulkDeleteView(BaseTeacherView, DeleteView):
    pass


def upload_teacher():
    pass
