# [Django REST Framework API](https://www.django-rest-framework.org/)
## Project - mysite
```bash
django-admin startproject mysite
```
### API App in mysite - `cd mysite`
```bash
python manage.py startapp api
```
## Setup
In `mysite.setting.py`, `INSTALLED_APPS[]`中，添加`api`, `rest_framework`

## `models.py`, `serializers.py`, `views.py`, `urls.py` 之间的关系

### `models.py`
Django 运用`ORM - Object relational mapping` 来将`python`对象映射到数据库实例中，在`Django`中，每一个`models.Model`的subclass对应一个数据库模型, 对该subclass的low level的操作（`create`, `update`, `retrieve`等）会映射到对应mapping关系的数据库中。
- 在`models.py`中，我们可以创建多个`model`,每个`model`对应一个数据库模版，却`model`和`model`中间可以建立一定的关系。
- 在`model`中，我们可以定义数据的列名以及属性（数据类型，长度等）。
### `serializers.py`
每当我们使用API时，实际上是在发送或是接送`json`数据。在`serializers.py`创建的`serializers.ModelSerializer`的subclass可以绑定特定的`model`,并将其转换为能与网页交互的`json - JavaScript Object Notation`兼容数据。
- 在`serializers.py`中，我们可以创建多个`serializers`,每个`serializers`对应一个`model`。实际实现为定义`model`变量并赋值具体`model`.
- 在`serializers.py`中，我们需要定义字段`fields`来定义想要在交互中返回的数据。
### `views.py` - Django Rest Framework Class based View
Django Rest Framework 提供一些用于创建、更新、删除等操作的默认视图`generics view`，在当中我们能执行标准的rest API CRUD数据操作。
- 在`views.py`中，我们可以为每个rest API操作（CRUD）创建一个视图（generics view的子类），每一个子类对应一个针对数据的操作。
- 每一个`view`子类需要定义一个`queryset`来指定该视图是针对哪个`model`的映射数据的`instance`的操作。
- 每一个`view`子类同样需要定义一个`serializer_class`来定义当我们对`model`映射的数据进行操作时所返回的`json`数据。
```py
from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create view based on generics view
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


# Retrieve, Update, Destroy View based on generics view  
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # primary key


### `urls.py`
Django 在创建的项目中提供了根路由`mysite->ulrs.py`,对于每个`app`建立的`urls.py`可以是根路由的延伸(forward).
以`path('api/', include("api.urls"))`为例，它是一个根路由下的`urlpattern`，根节点为`api/`，而斜杠后可以延伸`api.urls`中定义的路由`route`（或者说链接），这样对于任意`api`路由，我们都可以通过`server_url/api/route`来访问。
  - 若将上例改为`path('', include("api.urls"))`，则对于任意`api`路由，我们都可以通过`server_url/route`直接访问。
app中创建的`urls.py`允许我们为`view`视图创建对应的访问路由（或者说是链接），在访问对应的url时，我们会访问指定的视图，与API进行交互。
```py
from django.urls import path 
from . import views # 导入views

urlpatterns = [
    # 创建路由
    # 1. 定义url
    # 2. 指定对应的视图 views.classview.as_view()
    # 3. 定义名称
    path("blogposts/", views.BlogPostListCreate.as_view(),
         name="blogpost-view-create")
]
```
总结：
1. `model` 负责创建与数据列（属性）对应的模型模版;
2. `serializer` 负责将`model`定义的数据模型转化为可被识别，可交互的`json`形式;
3. `view` 定义对`model`, `serializer`所映射的数据进行CRUD操作的视图;
4. `url` 创建`view`视图所对应的路由地址，同时在project根路由中包含app `urls.py`中定义的路由

## Database Migration
每当对创建的`model`进行任何改动时（包括创建，更新，删除），都需要进行`migration`并应用`apply`，这实际上是借助Django ORM的特性，自动地创建SQL表或是针对SQL表进行任何基本的数据库操作。
```bash
python manage.py makemigrations # create the files that will specify what migrations need to be applied
python manage.py migrate # apply the migration
```

## 运行服务器
```bash
python manage.py runserver
```

## Appendix
- [HTTP Methods](https://www.restapitutorial.com/lessons/httpmethods.html)
- PUT, PATCH 的区别：PUT是对单个数据对象的全部更新（无论其中字段是否为局部更新），PATCH则可以完成局部更新，只更新实际更新了的字段。
- [Detailed descriptions, with full methods and attributes, for each of Django REST Framework's class-based views and serializers.](https://www.cdrf.co/)
