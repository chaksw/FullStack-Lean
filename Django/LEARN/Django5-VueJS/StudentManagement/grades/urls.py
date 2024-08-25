from django.urls import path
from .views import GradeListView, GradeCreateView, GradeUpdateView

urlpatterns = [
    path('', GradeListView.as_view(), name='grades_list'),
    path('create/', GradeCreateView.as_view(), name='grade_create'),
    path('<int:pk>/', GradeUpdateView.as_view(), name='grade_update')
]
