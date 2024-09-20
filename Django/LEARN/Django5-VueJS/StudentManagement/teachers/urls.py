from django.urls import path
from .views import (TeacherListView, TeacherCreateView, TeacherUpdateView,
                    TeacherDeleteView, TeacherBulkDeleteView)

urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers_list'),
    path('create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('bulk_delete/', TeacherBulkDeleteView.as_view(), name='teacher_bulk_delete'),
]
