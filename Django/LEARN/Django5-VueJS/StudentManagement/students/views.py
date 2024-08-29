from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
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
