# 1. Django + Vue Course
> 这个 README.md 作为 Django/LEARN/Django 课程的进阶延伸.

## 1.1. `URLS` 路由匹配模式 （`urls.py` 中的url路径定义方式）
### 1.1.1. 字符串精准匹配： 定义啥就识别啥
```python
# urls.py
path('hello/', helloWorld), # 只识别 'hello' or 'hello/' 地址
# name 的定义让我们可以在 template中通过name来访问该路由
path('acticle/create/', article_create, name='article_create'),  # 只识别 article/create地址
```
### 1.1.2. 路径转换器格式 `<type:value>` 一般用于访问符合特定属性的数据
```python
# urls.py
# 根据转换的类型不同，使用 <type:value> 格式， 如 `article_id` 是 `int`， 这定义为 `<int:article_id>`，访问格式必须满足转换器所定义的数据类型
path('article/<int:article_id>/', article_detail, name='article_detail'),

# views.py
# 使用路径转化器格式的 `url` 访问时相当于传递了 article_id 数据属性，所以对应的 view 函数中可以定义参数接收，以便后续访问该属性相关的数据
def article_detail(request, article_id):
    return HttpResponse(f'ID of article detail: {article_id}')

# urls.py
# 可以接受多个不同类型的属性｜数据，相应的访问规则也会变化
path('article/<int:article_id>/<str:title>/', article_detail, name='article_detail'),

# views.py
# 对应的 view 则定义相应的参数接收
def article_detail(request, article_id, title):
    return HttpResponse(f'ID of article detail: {article_id}, title: {title}')
```
### 1.1.3. 正则表达式：`re_path` 用于验证 `url` 是否满足特定字符匹配规则
```python
# 1. ^: 以什么开始，精准匹配字符
# 2. (?P<phone_number> 1[3456789]\d{9}) 一个捕获组，名字为phone_number， 必须以数字 1 开头， 第二位必须是 3、4、5、6、7、8 或 9 中的一个数字。 接下来的 9 位必须是数字 (0-9)
# 3. /$: 以 '/' 结尾
re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', phone_detail, name='phone_detail'),
```

### 1.1.4. 路由嵌套模式 - 根据应用将路由拆分
> 说白了就是将属于各个应用的url定义在各自的`urls.py`下，再引入到项目的`urls.py`中

```py
# 定义 app01 中的urls
# app01.urls.py
from django.urls import path, re_path
from app01.views import article_create, article_detail, phone_detail

urlpatterns = [
    path('create/', article_create, name='article_create'),
    # 路径转换器格式
    path('<int:article_id>/<str:title>/', article_detail, name='article_detail'),
    re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', phone_detail, name='phone_detail'),
]
# 用 `include` 导入 app01.urls
from django.contrib import admin
from django.urls import path, include
from app01.views import helloWorld, article_create, article_detail, phone_detail

urlpatterns = [
    # 精准匹配模式
    path('hello/', helloWorld),
    path('article/', include('app01.urls')),
    path('admin/', admin.site.urls),
]

# demo.urls.py
```

## 1.2. `VIEWS` 视图
> 视图在 `python` 中本质上就是一个视图函数 (`FBV`) 或者视图类 (`CBV`)，他们接收的永远是一个请求对象 (`request`), 并且返回一个相应对象 (`response`)

### 1.2.1. FBV - Function-Based View
> 这个章节是在应用 `account` 中实现的是一个基于 `FBV` 的用户登录功能

**要实现 `FBV` 视图功能需要一下步骤：**
1. 在全局的 `settings.py` 的 `TEMPLATES` 的 `'DIRS'` 元素中定义 `html` 文件所存储的路径，一般为项目根目录的 `tempaltes` 文件夹
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
2. 在 `tempaltes` 文件夹下创建 `.html` 文件
   1. 注意：对于用户登录的表单，需要定义 `form` `method` 为 `post`， 如果不定义默认会是 `get`，表单的信息会显示在提交的 `url` 中.
   2. 提交后，表单信息会提交到 `action` 的指定 `url` 下，如果 `action` 为空，则默认提交到当前 `url` 路径下, 也就是 `account/login`
   3. 对于 `post` 请求， `Django` 提供了 `CSRF` 保护机制(信息如下)，我们需要在每个 `method` 为 `post` 的表单中加入 `{% csrf_token %}`
> Reason given for failure:
>     CSRF token missing.
>     
> In general, this can occur when there is a genuine Cross Site Request Forgery, or when Django’s CSRF mechanism has not been used correctly. For POST forms, you need to ensure:
> 
> Your browser is accepting cookies.
> The view function passes a request to the template’s render method.
> In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
> If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
> The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.

```html
<!-- demo->templates->login.html-->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>
        <form action="" method="post">
            {% csrf_token %}
            <div>
                username:
                <input type="text" name="username">
            </div>
            <div>
                password:
                <input type="password" name="password">
            </div>
            <button>Login</button>
        </form>
    </div>
</body>

</html>
```
3. 在应用的 views 中定义 `FBV`，实现：
   1. 默认通过 `render` 函数引入 `.html` 文件，渲染登陆页面
   2. 实现相应的 `post` 请求的业务逻辑，只有在 `POST` 请求触发时才会执行
```py 
# account -> views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 接受请求，通过 render 函数引入希望渲染的html文件
def login(request):
    # post 请求的业务逻辑，只有在提交表达时才会触发
    # if request.method == 'POST' 等效
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 登陆业务逻辑，验证用户 ｜ 密码是否在数据库中等，这里模拟登陆成功的逻辑
        return HttpResponse(f'login success with {username} and password {password}')
    # 默认是 GET() 请求，渲染 login.html
    return render(request, 'login.html')
```

4. 在 `urls` 中进行路由和 `FBV` 的匹配
```py
# account -> urls.py
from django.urls import path
from .views import login

urlpatterns = [
    path('login/', login)
]

```

### 1.2.2. CBV - Class-Based View
> 相比起 `FBV` ， `CBV` 提供了更多的自定义配置和可拓展性
> 这个章节是在应用 `account` 中实现的是一个基于 `CBV` 的用户注册功能

**要实现 `CBV` 视图功能需要的步骤与 `FBV` 出了 `views.py` 内的实现外基本相同：**
1. 在全局的 `settings.py` 的 `TEMPLATES` 的 `'DIRS'` 元素中定义 `html` 文件所存储的路径，一般为项目根目录的 `tempaltes` 文件夹
2. 在 `tempaltes` 文件夹下创建 `.html` 文件

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>

<body>
    <div>
        <form action="" method="post">
            {% csrf_token %}
            <div>
                username:
                <input type="text" name="username">
            </div>
            <div>
                password:
                <input type="password" name="password">
            </div>
            <div>
                password confirm:
                <input type="password" name="password2">
            </div>
            <button>Register</button>
        </form>
    </div>
</body>

</html>
```

3. 在应用的 views 中定义 `CBV`，实现：
   1. `class` 的命名格式一般为驼峰
   2. `class` 继承于 `django` 的 `View`， `View` 作为父类包含了基于 `HTTP` 协议的交互方法, 这些方法对应不同的数据处理场景自动运行，我们只需要关注它们的业务逻辑实现。
      - `get(self, request)`：用于请求数据。
      - `post(self, request)`：用于提交数据以创建新的资源。
      - `put(self, request)`：用于更新现有资源。
      - `delete(self, request)`：用于删除资源

```py
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        return HttpResponse(f'login success with {username} and password {password}')
```

4. 在 `urls` 中进行路由和 `CBV` 的匹配
```py
# account -> urls.py
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register")
]

```

### 1.2.3. `FBV` & `CBV` 区别
**`FBV` 对于基于HTTP协议的交互方法的业务逻辑是通过判断 `request` 的 `http` 方法来展开的，这不利于复杂的业务逻辑，而 `CBV` 继承于 `django` 的 `View`， `View` 作为父类包含了基于 `HTTP` 协议的交互方法, 这些方法对应不同的数据处理场景自动运行，我们只需要关注它们的业务逻辑实现。**

### 1.2.4. `HttpRequest` & `HttpResponse` 的一些内容
#### 1.2.4.1. `HttpRequest` 
`HttpRequest` 包含两大基本数据
1. 请求头 `headers`： 一般通过 `HttpRequest.META.get('key')` 或者 `HttpRequest.headers.get('key')` 来获取请求头的对应信息 （`META` 比 `headers` 包含更多信息）
   
2. 请求参数： 根据不同的数据，获取方式不同：
   1. 获取 `GET` 参数: `value = request.GET.get('parameter_name', default_value)`
   2. 获取 `POST` 参数: `value = request.POST.get('parameter_name', default_value)`
   3. 获取 `URL` 参数: `value = request.GET.get('parameter_name', default_value)`, 与 `GET` 类似，但`parameter_name` 是 `url` 上的参数 （如 `?name=18&age=8`， 对应的参数为 `name` 和 `age`
   4. 获取请求体 （`request.body`）中的 `JSON` 参数: 通过 `build-in` 的 `json` 模块获取
```py
import json

data = json.loads(request.body) # 获取请求体并转化为json格式
value = data.get('parameter_name', default_value) # 通过key获取value
```
   5. 获取路径参数（即定义路由使用路径转换器是的 `id`）: 通过定义 `FBV` 中添加输入参数获取
```py
def my_view(request, parameter_name):
    # parameter_name 即 url 路径参数
```
   6. 获取请求头中的参数： `request.headers.get('parameter_name', default_value)`

#### 1.2.4.2. `HttpResponse`
可以通过在 `HttpResponse` 添加并更改响应头信息如 `headers`, `content-type` 等将响应数据传输到客户端
```py 
...
headers = {
    'token': 'Chris',
}
return HttpResponse(f'login success with {username} and password {password}', content_type="text/html; charset=utf-8", status=200, headers=headers)

```
另外的还有一种 `JsonResponse`, 返回的是一个 `dict` 数据，响应数据中的 `content-type` 为 `application/json`
```py 
...
res = {
    'name': username,
    'password': password,
    'status': 200,
    'message': OK
}
return JsonResponse(res)

```

## 1.3. `Tempaltes` 模版
1. 关于模版引擎和配置关注 `settings.py` 中的 `INSTALLED_APP` 和 `TEMPLATES`
2. 关于模版的语法知识和继承可以在 `LEARN/Django/README.md` 的 Section 1.2. Template and Django template language 中了解 
3. 关于 `{% include '*.html'%}` 的用法后续用到后再补充，简单来说就是将一个简单的组件式 `html` 通过 `include` 引入到别的 `html` 中


## 1.4. `Model` 数据模型

### 1.4.1. 关键概念：对象关系映射 - ORM (Object Relational Mapping) 

> `FullStack-Lean/Django/PRACTICE/Django-REST-API/README.md` section 1.3 中也有记录
Django 运用`ORM - Object relational mapping` 来将`python`对象映射到数据库实例中，在`Django`中，每一个`models.Model`的 `subclass` 对应一个数据库中的数据表格, 每一个类的对象对应着一个数据行，对该 `subclass` 对象的low level的操作（`create`, `update`, `retrieve`等）对应对数据库的SQL语句操作。
### 1.4.2. 对应关系
1. 数据表 - 类
2. 数据行 - 对象
3. 字段 - 对象属性
### 1.4.3. 数据库 `mysql` 的配置和创建
#### 1.4.3.1. 前期配置 
```bash
# 1. 安装
brew install mysql # 也可以通过安装包安装
# 1.1 如果出现 Can't connect to local MySQL server through socket '/tmp/mysql.sock' 执行1.2-1.4
# 1.2 获取sock路径(用于与服务器通信的套接字文件)，输出为/tmp/mysql.sock，按往后实际为准
mysql_config --socket 
# 1.3 分配读写，执行权限
sudo chmod 2777 /tmp/mysql.sock # 
# 1.4 验证更改
ls -l /tmp/mysql.sock # 输出为 s-w-rwxrwx  1 RunshengWU  wheel  0 10 aoû 10:22 /tmp/mysql.sock
# 2. 链接 mysql 初次链接用户名为 root, 密码为空(直接 enter 即可)
mysql -u root -p
```
#### 1.4.3.2. 配置
> `Django` 默认使用的是 `sqlite3`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'django_demo',  # 数据库名称
        'HOST': '127.0.0.1',  # 主机名
        'USER': 'root',  # 用户名
        'PASSWORD': '',  # 密码
    }
}
```

#### 1.4.3.3. 创建
```bash
# 链接 mysql 初次链接用户名为 root, 密码为空(直接 enter 即可)
mysql -u root -p
# 创建 django_demo
create database django_demo;
```

#### 1.4.3.4. 使用数据库引擎 `PyMySQL` 链接数据库(错误操作请忽略)
> NOTE: (课程步骤有错误无法运行)
```bash
pip install pymysql
```

```py
# __init__.py 
import pymysql
pymysql.install_as_MySQLdb()
```
#### 1.4.3.5. 使用数据库引擎 `mysqlclient` 链接数据库 
> NOTE: (重要：`PyMySQL` `mysqlclient` 只能有一个安装在pip上 )
```bash
pip install mysqlclient # 先确保PyMySQL已经卸载且项目上没有pymysql.install_as_MySQLdb()
``` 
#### 1.4.3.6. 执行数据库迁移
```bash
python manage.py migrate
# 输出：
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying sessions.0001_initial... OK
```

#### 1.4.3.7. 验证表格是否创建
```bash
mysql -u root -p # 进入mysql

use django_demo # 调用数据库

show tables; # 显示创建的表格
# 输出：
# table名字为 app_tablename: 如 auth_user为 auth 应用下的 user
+----------------------------+
| Tables_in_django_demo      |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
10 rows in set (0,01 sec)

```

### 1.4.4. `models.py`
> NOTE: 要应用模型数据，需要先确保 `INSTALLED_APP` 中有对应模型的应用

#### 1.4.4.1. 字段类型
<img src='/Users/Chaksw/Web-Dev/FullStack-Lean/Django/LEARN/Django5-VueJS/assets/imgs/字段类型1.png' alt='字段类型'>
<img src='/Users/Chaksw/Web-Dev/FullStack-Lean/Django/LEARN/Django5-VueJS/assets/imgs/字段类型2.png' alt='字段类型'>


#### 1.4.4.2. 创建模型
> 代码见下章 节- 设置 `meta` 元数据

#### 1.4.4.3. 执行并应用数据迁移
> 迁移文件的创建让项目的迁移更方便，在别的机器上运行该项目时，只需要直接运行应用迁移文件的命令就可以创建一个相同的数据库了
1. 创建迁移文件
```bash
python manage.py makemigration
```
2. 应用迁移文件
```bash
python manage.py migrate
```

#### 1.4.4.4. 设置 `meta` 元数据 (基础应用)
1. 创建一个 `baseModel` 用于创建基础共用字段，需要共用字段的模型可以继承于这个模型，base表只需要被继承，不需要创建在数据库中，所以设置元数据 abstract = True
```py
# in utils.py 
from django.db import models


class BaseModel(models.Model):
    # auto_now_add 自动填入目前时间
    # editable: 控制是否可编辑
    create_at = models.DateTimeField('createTime', auto_now_add=True, editable=True)
    update_at = models.DateTimeField('updateTime', auto_now_add=True, editable=True)

    # Base表只需要被继承，不需要创建在数据库中，所以设置元数据 abstract = True
    class Meta:
        abstract = True
```

```py
# account.models.py
from django.db import models
from utils.basemodels import BaseModel
# Create your models here.


class User(BaseModel):
    class Meta:
        db_table = 'user'  # 表名 (数据表中显示的名称)
        verbose_name = 'userInfo'  # 显示在前端的名称
    # AutoField 自增
    id = models.AutoField(primary_key=True)
    # verbose_name： 别名，页面显示时的名字
    # null 控制是否允许在数据库上为空
    # blank 控制是否允许在页面显示时为空
    # unique 控制值是否唯一
    username = models.CharField(verbose_name='username', max_length=30, null=True, blank=True, unique=True)
    passworkd = models.CharField(verbose_name='password', max_length=30)
    email = models.EmailField(verbose_name='email', null=True, blank=True, unique=True)

```

```py
# app01.models.py
from django.db import models
from account.models import User
from utils.basemodels import BaseModel

# Create your models here.


class Article(BaseModel):
    class Meta:
        db_table = 'article'  # 设置表名 (数据表中显示的名称)
        verbose_name = 'articleInfo'  # 显示在前端的名称
        ordering = ['-publish_date']  # 以publish_date 降序， 发布越晚越靠前
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='title', max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

```bash
# 添加 meta后的 tables
+----------------------------+
| Tables_in_django_demo      |
+----------------------------+
| article                    |
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| user                       |
+----------------------------+
12 rows in set (0,00 sec)
```

#### 1.4.4.5. ORM 增删改查 - CRUD
- C - create
- R - read
- U - update
- D - delete

#### 1.4.4.6. 使用 `shell` 进行 `django` 数据的 `CRUD`
```bash
python manage.py shell # 进入 shell
```
#### 1.4.4.7. ORM 新增｜插入数据
- C - Create：新增数据方式
   1. 保存一条数据 `save()`
   2. 新增一条数据 `create()`
   3. 批量新增数据 `bulk_create()`
1. `save()`
```bash
# 使用 shell 演示：
>>> from account.models import User # 导入 User 模型
>>> user_obj = User(username='chris', password='123456', email='test@email.com') # 创建数据行
>>> user_obj.save() # 保存
```
2. `create()`
```bash
>>> user2 = User.objects.create(username='chaksw', password='123456', email='test2@email.com')
```
3. `bulk_create()`
```bash
>>> user4 = User(username='chris4', password='123456', email='test4@email.com')
>>> user5 = User(username='chris5', password='123456', email='test5@email.com')
>>> user_list = [user4, user5]
>>> User.objects.bulk_create(user_list) # bulk_create()
[<User: User object (None)>, <User: User object (None)>]
```
4. 创建包含外键 `ForeignKey` 的数据 
创建包含外键 `ForeignKey` 的数据时，需要指定外键
```bash
>>> from app01.models import Article
# 导入 datetime 使用 datetime.now()
>>> from datetime import datetime
# 指定外键 user=user_obj
>>> article1 = Article(title='first article', content='the first article', publish_date=datetime.now(), user=user_obj)
>>> article1.save()
```

#### 1.4.4.8. ORM 查询数据
- R - Read: 查询数据方式
  1. 返回所有数据 `all()`
  2. 按照查询条件返回单条数据 `get(**kwargs)`
  3. 按照查询条件返回多条数据 `filter(**kwargs)`
  4. 返回最晚｜最早一条记录 `latest(*fields)`/`earlist(*fields)`
  5. 返回第一条｜最后一条记录 `first()`/`last()`
1. `all()`
```bash
>>> from account.models import User
>>> user = User.objects.all() # 使用 all() 获取所有数据
>>> user
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

2. `get(**kwargs)`
> NOTE：如果查询记录不存在或是返回数据大于1条，会报错
```bash
# 根据 username 查询
>>> user = User.objects.get(username='chris')
>>> user.id, user.username, user.password, user.email
# 输出
(1, 'chris', '123456', 'test@email.com')
# 根据 id 查询
>>> user = User.objects.get(id=2)
>>> user.id, user.username, user.password, user.email
(2, 'chaksw', '123456', 'test2@email.com')
```

3. `filter(**kwargs)`
```bash
# id__gt: id 大于 1， filter返回的是一个object list（QuerySet）
>>> User.objects.filter(id__gt=1)
<QuerySet [<User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

4. `latest(*fields)`/`earlist(*fields)`
```bash
# 没有演示。。。
```

5. `first()`/`last()`
```bash
# first()
>>> user = User.objects.first()
>>> user.username
'chris'
# last()
>>> user = User.objects.last()
>>> user.username
'chris5'
```

#### 1.4.4.9. ORM 查询条件1: 基础
- Conditional Search 1
1. 相等/等于/布尔条件 
   1. `field__exact`/`field__iexact()`
   2. `field__gt`/`field__gte`/`field__lt`/`field__lte`，通常比较的是数值字段
   3. `filed__isnull`
2. 是否包含**字符串 `field__icontains`/`field__contains`/`field__in`
3. 以**开始/结束 `field__startswith`/`field__endswith`/`field__istartswith`/`field__iendswith`
4. 日期及时间 `create_at`/`update_at` 拼接 `__year`/`__month`/`__day`/`__hour/minute/second`/`__week/week_day`
5. 外键关联

6. 相等/等于/布尔条件
```bash
# field__exact
>>> User.objects.get(id__exact=2)
<User: User object (2)>
# field__iexact， 不区分大小写
>>> user = User.objects.get(username__iexact='Chris')
>>> user.username
'chris'
# field__lte
>>> User.objects.filter(id__lte=3)
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]
# filed__isnull
>>> User.objects.filter(username__isnull=True)
<QuerySet []>
# field__in
>>> User.objects.filter(id__in=[2,4,6])
<QuerySet [<User: User object (2)>, <User: User object (4)>]>
```

1. 是否包含**字符串
```bash
# field__contains
>>> User.objects.filter(username__contains='ch')
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
# field__icontains： 不区分大小写
>>> User.objects.filter(username__icontains='Ch')
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

3. 以**开始/结束
```bash
# field__startwith
>>> User.objects.filter(username__startswith='ch')
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

4. 日期及时间
```bash
# create_at__year
>>> User.objects.filter(create_at__year=2024)
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

5. 外键关联
```bash
# 通过关联外键名__外键字段查询，如果是filter返回的是一个object list（QuerySet）
article1 = Article.objects.filter(user__username='chris')
>>> article1
<QuerySet [<Article: Article object (1)>]>
# 如果是 get 返回的是一个 object
article1 = Article.objects.get(user__username='chris')
>>> article1
<Article: Article object (1)>
```

#### 1.4.4.10. ORM 查询条件2: 多条件查询
- Conditional Search 2
    1. 使用 `filter()` 时指定多个条件 （仅支持 `&`）
    2. `Q()` 函数，支持 `&` 和 `｜`
1. 使用 `filter()` 时指定多个条件 （仅支持 `&`）
```bash 
# 方式1: 使用多个filter()
>>> User.objects.filter(create_at__month=8).filter(username__contains='ch')
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
# 方式2: 用 & 串联两个 objects.filter()
>>> User.objects.filter(create_at__month=8)&User.objects.filter(username__contains='ris')
<QuerySet [<User: User object (1)>, <User: User object (4)>, <User: User object (5)>]>
```

2. `Q()` 函数，支持 `&` 和 `｜`
```bash 
# Q() 函数是 Django 的一个便捷函数
>>> from django.db.models import Q
# 创建一个 query (过滤条件)
>>> query = Q(create_at__month=8) & Q(username__contains='ris')
# 使用 query
>>> User.objects.filter(query)
<QuerySet [<User: User object (1)>, <User: User object (4)>, <User: User object (5)>]>
# 使用 |
>>> query = Q(create_at__month=8) | Q(username__contains='ris')
>>> User.objects.filter(query)
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>]>
```

#### 1.4.4.11. ORM 修改数据
- U - Update: 修改数据方式
   1. 修改单条数据 `save()`
   2. 批量修改数据 `update()`
   3. 批量修改数据 `bulk_update()`

1. 修改单条数据 `save()`
```bash
# 获取要修改的数据
>>> user = User.objects.get(username='chris')
>>> user.email
'test@email.com'
# 修改数据
>>> user.email = 'chris@email.com'
# 保存修改
>>> user.save()
# 验证修改
>>> user.email
'chris@email.com'
```

2. 批量修改数据 `update()`
```bash
# 先使用 filter 获取 QuerySet 数据，要用update进行修改，如果修改成功返回 1
>>> status = User.objects.filter(id=2).update(password='33333', email='idis2@email.com')
>>> status
1
# 可以将获取数据和修改数据两步拆分
>>> user = User.objects.filter(id=2)
>>> user
<QuerySet [<User: User object (2)>]>
>>> user.update(password='444444')
1
>>> user[0].password
'444444'
# 对于 update() 不能使用 get 获取数据
>>> user = User.objects.get(id=2).update(password='33333', email='idis2@email.com')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'User' object has no attribute 'update'

# 修改外键同理
>>> article = Article.objects.get(id=1)
>>> article.user
<User: User object (1)>
>>> user2 = User.objects.get(id=2)
# user 为外键关联字段名
>>> Article.objects.filter(id=1).update(user=user2)
1
```

3. 批量修改数据 `bulk_update()`
```bash
# 没演示，听说不常用
```

#### 1.4.4.12. ORM 删除数据
- D - Delete
    1. 物理删除 `delete()`
    2. 逻辑删除，为数据增加状态属性，如果属性为1就显示，为0则不显示，但实际数据没有删除，所以准确来说是控制显示
1. 物理删除 `delete()`
```bash
# 用filter()获取数据
>>> user5 = User.objects.filter(id=5)
# 执行删除
>>> user5.delete()
(1, {'account.User': 1}) #不知道为啥会出现
# 也可以用 get() 获取数据
>>> user4 = User.objects.get(id=4)
# 执行删除
>>> user4.delete()
(1, {'account.User': 1})
# 也可以删除多条
>>> users = User.objects.all()
# 原本有3个数据
>>> users
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]>
# 获取 username 包含 'w‘ 的要删除的数据
>>> usersToDelete = User.objects.filter(username__contains='w')
>>> usersToDelete
<QuerySet [<User: User object (2)>, <User: User object (3)>]>
# 执行删除
>>> usersToDelete.delete()
(3, {'app01.Article': 1, 'account.User': 2})
# 验证删除
>>> users = User.objects.all()
>>> users
<QuerySet [<User: User object (1)>]>
```

2. 逻辑删除
```bash
# 没演示。。。
```

### 1.4.5. `Django` 的管理后台 `admin`
1. 关于Django` 的管理后台 `admin 的知识可以在 `LEARN/Django/README.md` 的 Section2. Django Admin 中了解
2. 这里结合点 1 做一些补充的记录
3. 
#### 1.4.5.1. 创建超级管理员
```bash
python manager.py createsuperuser
# enter username, email and password
```

#### 1.4.5.2. 配置页面为中文及中国时区（可选）
```py
# 在 `settings.py` 中
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

```

#### 1.4.5.3. 创建 `admin` 数据模型并绑定模型
> 代码见后台配置章节

### 1.4.6. 后台配置 
1. 更好后台的 app 名称（增加别名）
```py
# account.apps.py
# 使用 verbose_name
from django.apps import AppConfig

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    verbose_name = 'Account Management' # admin 后台显示的 title 名称
```
2. 更改 admin 后台数据模型名称
```py
# account.models.py
# 使用 verbose_name_plural
...
class User(BaseModel):
    class Meta:
        db_table = 'user'  # 表名 (数据表中显示的名称)
        verbose_name = 'userInfo'  # 显示在前端的名称
        verbose_name_plural = 'User Information' # 后台模型名称 (admin 后台显示的表名称)
   ...

```
3. 设置只读字段 `readonly_fields`
4. 为字段设置可到详情页的链接 （默认只有 `id` 字段可以跳转）`list_display_links`
5. 设置直接修改功能（不需要跳转到详情页再修改） `list_editable`
**注意：对于同一个字段不能同时设置 `list_display_links` 和 `list_editable`**
```py
# account.admin.py
from django.contrib import admin
from account.models import User
# Register your models here.

# 创建 admin 数据模型， class 名字一般为 ModelNameAdmin
# 继承于 ModelAdmin 的类已经实现了 CRUD 功能
class UserAdmin(admin.ModelAdmin):
    # 定义显示显示在 admin 页面的字段
    list_display = ('id', 'username', 'email')
    # 配置可供过滤的字段
    list_filter = ('username', 'email')
    # 配置搜索框，定义可供搜索的字段
    search_fields = ('username', 'email')
    # 在当前 django 版本中 id 默认只读，所以 comment 掉
    # readonly_fields = ('id',)
    # 设置可跳转到详情页的字段
    list_display_links = ('id', 'username')
    # 设置直接修改功能
    list_editable = ('email',)


# 将数据模型与admin数据模型绑定
admin.site.register(User, UserAdmin)
```

```py
# app01.admin.py
# 使用 readonly_fields 设置只读字段
# 使用 list_display_links 设置可跳转到详情页的字段
# 使用 list_editable 设置直接修改功能（不需要跳转到详情页再修改） 
from django.contrib import admin
from app01.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'user')
    # 配置可供过滤的字段
    list_filter = ('title', 'content', 'user')
    # 配置搜索框，定义可供搜索的字段，注意外键不能作为可供搜索的字段
    search_fields = ('title', 'content')
    # 在当前 django 版本中 id 默认只读，所以 comment 掉
    # readonly_fields = ('id',)
    # 设置可跳转到详情页的字段
    list_display_links = ('id', 'title')
    # 设置直接修改功能
    list_editable = ('content',)


admin.site.register(Article, ArticleAdmin)
```

### 1.4.7. 自定义函数增加字段
自定义函数，将 `Article` 的外键 `user` 的字段 `username` 作为新的字段 `author`
```py
# app01.admin.py
from django.contrib import admin
from app01.models import Article
# Register your models here.


# 自定义函数，返回外键的 username user.username
def get_author(obj):
    return obj.user.username


class ArticleAdmin(admin.ModelAdmin):
    # 将函数作为字段写入后台显示
    # django 会在使用 list_display 时给 get_author 传递 ArticleAdmin 的实例对象
    list_display = ('id', get_author, 'title', 'content', 'user')
    # 配置可供过滤的字段
    list_filter = ('title', 'content', 'user')
    # 配置搜索框，定义可供搜索的字段，注意外键不能作为可供搜索的字段
    search_fields = ('title', 'content')
    # 设置可跳转到详情页的字段
    list_display_links = ('id', 'title')
    # 设置直接修改功能
    list_editable = ('content',)


# 使用 short_description 将 get_author 的字段 header 更名为 'author'
get_author.short_description = 'author'
admin.site.register(Article, ArticleAdmin)
```

### 1.4.8. 补充：更改外键在编辑（详情）页的显示
```py
# account.admin.py
...
class User(BaseModel):
    ...
    # 设置 __str__, 当需要输出（显示）User 实例时，会自动调用，显示对应 return 的值
    def __str__(self):
        return self.username

```

## 1.5. Student Management 项目

### 1.5.1. 在当前目录下创建项目
假设已有文件夹 project，当运行：
```bash
django-admin startproject project
```
会在 project 文件夹下创建：
```bash
- project # 已有文件夹
    - project # startproject project 对应的文件夹
        - project # 包含settings.py 等文件
        - manage.py
```
如果希望以 project 为项目根路径，创建如下结构：
```bash
- project # 已有文件夹
    - config # 包含settings.py 等文件 (名为 config)
    - manage.py
```
可以使用:
```bash
django-admin startproject config .
```
### 1.5.2. 重命名项目名称
如果要更改项目名称：如 `website` 项目中将包含 `settings.py` 的 `website` 文件夹重命名为 `config`，出了文件夹名字更改外，还需要将：
```py
# in settings.py 
# ROOT_URLCONF = 'website.urls' 更改为：
ROOT_URLCONF = 'config.urls'
# WSGI_APPLICATION = 'website.wsgi.application' 更改为：
WSGI_APPLICATION = 'config.wsgi.application'

# in asgi.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings') 更改为:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'):


# in wsgi.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings') 更改为：
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# manage.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings' 更改为：
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
```

### 1.5.3. 静态文件的相关配置
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# STATIC 路径主要用于处理项目需要引用的静态文件
# 作用是能通过url直接访问在项目中的静态文件 (CSS, JavaScript, 图片等)
STATIC_URL = 'static/'
# 它的定义是告诉 django， 首先在 STATICFILES_DIRS 搜寻静态文件，其次再到各个app的 static文件夹里面找
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# media setting
# MEDIA 路径主要用于处理用户上传的媒体文件（图片，视频，文档等)
# 用于拼接静态文件的存储路径，后续在 views.py 中进行相应设置，可让 media 下的静态文件暴露在前端中, 通过 url 进行对应的静态文件访问
MEDIA_URL = '/media/'
# 静态文件的存储路径，与 MEDIA_URL 相对应，当html需要链接对应静态文件时，可通过静态文件对应的变量如： 'media/{{ data.images }}来定义静态文件的 url。当客户访问 media 相关的 url 时，实际是在该路径下读取相关的静态文件，
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 要达到上述效果，需要在 views.py中设置
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.MEDIA_URL, document_roort=settings.MEDIA_ROOT)

# 配置 ckeditor 富文本，就是 rtf 格式文档， rtf文档中可以潜入图像，链接等文件格式。富文本的引用可以让我们在后台编辑数据是有更丰富的选择，同时前端也会像是相应的字体，图片，链接等富文本样式
CKEDITOR_UPLOAD_PATH = 'upload/'  # 富文本文件的上传路径
CKEDITOR_IMAGE_BACKEND = 'pillow'  # 富文件上传图片的后台
# 对应的 models 中使用富文本可以导入并使用 RichTextField，如果需要上传图片，则导入并使用 RichTextUploadingField
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
```
### 1.5.4. 表单悬浮窗口实现以及表单数据验证流程
1. 在项目跟 `urls.py` 中建立根路由
2. 建立数据表：定义 `models.py` 中的CBV，
3. 建立路由：定义 `urls.py`, 建立创建数据模型对应的 url
4. 建立视图功能，实现 request <-> response 交互逻辑：定义 `views.py` 中 `CreateView` | `UpdateView` 的 model view，与 url 进行绑定（`as_view()`），并定义表单验证成功 `form_valid()` 以及失败 `form_invalid()` 方法，返回对应的 `Response` 数据。
5. 建立数据-路由-模板的联系：在 `modelView`，中定义 `model`, `form_class`, `template_class`，将数据表，表单，前端显示页面绑定
6. 建立数据显示界面：在 `<model>_list.html` 中给定新建按钮跳转路径为给定 url，并通过 `sweetalter2` 实现浮窗效果
7. 建立表单：定义 `forms.py` 建立对应的数据表对应的表单模型，并通过定义 `clean_<field_name>` 创建每个字段的验证方法。
8. 建立表单显示界面：定义 `<model>_form.html`，建立表单的前端显示页面
9. 实现 submit 功能：在 `<model>_form.html` 中，使用 `fetch` 实现 `submit` 异步请求，并对 model view 中成功 `form_valid()` 以及失败 `form_invalid()` 所返回的数据进行处理，将相关数据以特定方式显示在前端。


### 1.5.5. `CreateView`
```py
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_class = 'students/student_form.html'
    # success_url = reverse_lazy('students_list')
    # 当 type='sumbit' 的按钮按下后，会提交表单，产生一个 post 请求，将表单数据发送到服务器
    # 服务器接收到数据后，CreateView 会调用 ModelForm 中的各种方法，包括 form.is_valid(), clean_<field_name> 方法来验证数据是否合法
    #
    # 如果数据有效，默认情况下 form_valid() 会被执行， 其中会自动调用 form.save() 将数据保存到数据库中，（如果重写了 form_valid()，则不会自动调用 form.save(), 而需要显示调用)
    # 如果数据保存，会重定向到 success_url 中指定的页面
    # 表单字段验证

    def form_valid(self, form):
        # 接收字段
        student_name = form.cleaned_data.get('student_name')
        student_number = form.cleaned_data.get('student_number')
        # 写入 auth_user 表，username为 student_name + student_number, 密码为 student_number 后6位
        username = f"{student_name}_{student_number}"
        password = student_number[-6:]
        users = User.objects.filter(username=username)
        if users.exists():
            # 如果已存在相同 username 的 user
            user = users.first()
        else:
            # 如果不存在，使用 django 自带的 User.objects.create_user(), 该方法会自动对密码进行加密
            user = User.objects.create_user(username=username, password=password)
        # 将用户写入 student, 模型实例关联
        form.instance.user = user
        form.save()
        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    # 重写父类方法，定义表单验证失败时的逻辑
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)

```


### 1.5.6. `ModelForm`
- ModelForm 根据与之关联的模型自动生成表单字段。每个模型字段都对应一个表单字段。例如，CharField 转换为 forms.CharField，DateField 转换为 forms.DateField，等等。
- ModelForm 自动继承并执行模型定义中的验证逻辑，如字段的 max_length、unique、blank、null 等约束条件。
- ModelForm 提供了 clean() 方法，可以对整个表单的数据进行验证和清理。你还可以为特定字段定义 clean_<fieldname>() 方法，以对单个字段进行自定义验证和清理。
- ModelForm 提供了 save() 方法，允许你轻松将表单数据保存到数据库。默认情况下，它会将表单数据保存为与模型关联的新对象，或者更新现有对象。
```py
# 例子：student_management 中的 student->forms.py
import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Student
from grades.models import Grade


class StudentForm(forms.ModelForm):
    # 重写 form 的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 重新定义 外键 grade 为 Grade 的 object，并以 grade_number 进行排序（默认升序）
        self.fields.get('grade').queryset = Grade.objects.all().order_by('grade_number')
    # 定义字段验证方法： clean_<field_name>

    def clean_student_name(self):
        # self.cleaned_data 为提交的全部表单信息
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 2 or len(student_name) > 50:
            raise ValidationError('请填写正确的学生名')
        return student_name

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if len(student_number) != 19:
            raise ValidationError('请填写正确的学籍号（长度应为19位）')
        return student_number

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if not isinstance(birthday, datetime.date):
            raise ValidationError('生日日期格式错误，正确格式为如：2024-05-01')
        if birthday > datetime.date.today():
            raise ValidationError('生日日期不能大于今天')
        return birthday

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if len(contact_number) != 11:
            raise ValidationError('请填写正确的手机号（长度应为11位）')
        return contact_number

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['student_name', 'student_number', 'grade', 'gender', 'birthday', 'contact_number', 'address']

```

### 1.5.7. 使用 `fetch` 实现 `submit` 异步请求
> 通过使用 `fetch` 实现异步请求，使得新的请求不会阻塞页面（同步请求需要我们跳转到新的页面），同时它能更精细的控制请求的细节（请求头，请求方法，请求体等），这样可以实现 `CURD` 时不加载新的页面，而是弹出悬浮框。
### 1.5.8. 使用 `fetch` 实现 `submit` 异步请求
> 通过使用 `fetch` 实现异步请求，是的新的请求不会阻塞页面（同步请求需要我们跳转到新的页面），同时它能更精细的控制请求的细节（请求头，请求方法，请求体等），这样可以实现 `CURD` 时不加载新的页面，而是弹出悬浮框。

```js
// student_management 中的 student_form.html

// 监听 DOM 是否有内容加载完成
document.addEventListener('DOMContentLoaded', () => {
    // 选择 html 中的第一个 form 元素
    const form = document.querySelector('form')
    // 定义 CURD 对应的 url 
    const url = "{% url 'student_create' %}"
    // 监听 form 的 submit 事件
    form.addEventListener('submit', function (e) {
        e.preventDefault(); // 阻止默认提交
        // 获取表单数据
        let formData = new FormData(form)
        // 使用 fetch 发送请求 （以定义更多自定义内容）
        // 在fetch中定义了发送request的目标（url,以及请求（request)信息
        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                // 添加 csrf-token 以防报错
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
            // fetch 会返回以一个 'Promise', 通过 then() 方法可以处理服务器的响应
        }).then(response => response.json()) // 将响应解析为 JSON 格式
            .then(data => { // 通过另一个 then() 会调处理解析后的数据
                // 发送的服务器后，服务器，也就是django views 中会运行 form_valid() 等函数进行数据验证操作，在 form_valid中，我们可以自定义数据验证（见 StudentCreateView() 中的 form_valid）的操作，并定义响应的内容（如 status, messages 等）
                if (data.status === 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: data.messages,
                        text: '数据已成功提交'
                    }).then((result) => {
                        if (result.value) {
                            // 提交成功后，回到窗口父页面并刷新
                            window.parent.location.reload()
                        }
                    })

                } else {
                    // 接受错误信息
                    // 解析嵌套的 JSON 字符串为 errors 对象
                    const errors = JSON.parse(data.messages)
                    // errors 结构为：["student_name": ["message": "...", "code": "..."], ...]
                    // 构造错误文本
                    let errorMessage = '';
                    // 遍历 errors 对象的每一个属性
                    for (const field in errors) { // filed 为 ["student_name":[], "student_number": [], ...]
                        // errors.hasOwnProperty(field) 确保这个字段是对象的直接属性，而不是继承自原型链。
                        if (errors.hasOwnProperty(field)) {
                            // 处理每个错误字段，每个字段 errors[field] 是一个数组，包含了与该字段相关的所有错误信息
                            errors[field].forEach(error => { // error 为 ["message": "...", "code": "..."]
                                errorMessage += `<li style="color:red;text-align:left;margin-left:100px;"> ${error.message} </li>`
                            })
                        }
                    }
                    Swal.fire({
                        icon: "error",
                        title: "提交错误",
                        html: errorMessage,
                        confirmButtonText: "关闭"
                    })
                }
            }).catch((error) => {
                Swal.fire({
                    icon: 'error',
                    title: '网络请求失败',
                    text: '无法连接到服务器，请稍后再试',
                    confirmButtonText: '关闭'
                })
            })
    })
})
```


### 1.5.9. `request` 和 `self.request` 的区别
在 Django 中， `request` 和 `self.request` 都指的是 HTTP 请求对象，但它们的**使用场景**和**上下文**有所不同：

1. `request` （作为参数传递的请求对象）
    - `request` 是在基于函数的视图（Function-Based Views，FBV）和基于类的视图（Class-Based Views，CBV）的方法中作为参数显式传递的。   
    - 它通常代表当前的 HTTP 请求对象，包含了所有与请求相关的数据，如请求方法、用户信息、GET 和 POST 数据等。
2. `self.request`（作为类实例的属性）
    - `self.request` 是在基于类的视图（Class-Based Views，CBV）中使用的，是视图实例的一个属性，表示当前的 HTTP 请求对象。
    - 在基于类的视图中，`self.request` **是自动从请求中提取并存储在视图实例中的**，因此你不需要显式地将 request 作为方法参数传递。
3. 在 Django 的 DeleteView 或其他基于类的视图（CBV）中，`self.request` 和 `request` 在方法中的确本质上是同一个对象。它们都指向当前的 HTTP 请求对象，包含相同的数据和信息（如请求方法、用户信息、GET/POST 数据等）。