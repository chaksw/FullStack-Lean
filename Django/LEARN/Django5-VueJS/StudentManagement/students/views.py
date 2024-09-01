from django.db.models.query import QuerySet
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
    # success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        # 表单字段验证

        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        })
