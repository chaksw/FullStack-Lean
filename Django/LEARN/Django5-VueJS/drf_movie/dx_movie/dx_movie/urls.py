"""
URL configuration for dx_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from movie import views

router = DefaultRouter()
# 每个 viewset 都可以通过路由注册的方式，即可想所有 urls 的 CURD 资源导入，而在 urlpatterns 中只需要 include(router.urls) 即可，也不需要在每个app文件夹下定义 urls.py
#
router.register(r'movie', views.MovieViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/movie/', include("movie.urls", namespace='movie')),
    path('api/', include(router.urls)),

]
