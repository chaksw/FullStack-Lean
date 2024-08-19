from django.urls import path, include
from news import views

urlpatterns = [
    path('list/', views.new_list),
    path('<int:id>/', views.detail),
]
