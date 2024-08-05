from django.urls import path, re_path
from app01.views import article_create, article_detail, phone_detail

urlpatterns = [
    path('create/', article_create, name='article_create'),
    # 路径转换器格式
    path('<int:article_id>/<str:title>/', article_detail, name='article_detail'),
    re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', phone_detail, name='phone_detail'),
]
