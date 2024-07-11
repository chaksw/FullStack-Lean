"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import TodoView
from rest_framework import routers

# router allows us to make some queries
# it define a path ("tasks") that return a list of Todo data list (defined in TodoView), where CURD operations can be done
# also it allows we can add 'id' (primary key) after path to return a single todo item, and CURD operations can be done
routers = routers.DefaultRouter()
routers.register(r'tasks', TodoView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TodoView.as_view(), name="todoList")
    path('api/', include(routers.urls))
]
