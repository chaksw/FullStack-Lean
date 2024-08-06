# Django + Vue Course
> 这个 README.md 作为 Django/LEARN/Django 课程的进阶延伸.

## `URLS` 路由匹配模式 （`urls.py` 中的url路径定义方式）
### 字符串精准匹配： 定义啥就识别啥
```python
# urls.py
path('hello/', helloWorld), # 只识别 'hello' or 'hello/' 地址
# name 的定义让我们可以在 template中通过name来访问该路由
path('acticle/create/', article_create, name='article_create'),  # 只识别 article/create地址
```
### 路径转换器格式 `<type:value>` 一般用于访问符合特定属性的数据
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
### 正则表达式：`re_path` 用于验证 `url` 是否满足特定字符匹配规则
```python
# 1. ^: 以什么开始，精准匹配字符
# 2. (?P<phone_number> 1[3456789]\d{9}) 一个捕获组，名字为phone_number， 必须以数字 1 开头， 第二位必须是 3、4、5、6、7、8 或 9 中的一个数字。 接下来的 9 位必须是数字 (0-9)
# 3. /$: 以 '/' 结尾
re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', phone_detail, name='phone_detail'),
```

### 路由嵌套模式 - 根据应用将路由拆分
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

## `VIEWS` 视图
> 视图在 `python` 中本质上就是一个视图函数 (`FBV`) 或者视图类 (`CBV`)，他们接收的永远是一个请求对象 (`request`), 并且返回一个相应对象 (`response`)

### FBV - Function-Based View
> 这个章节实现的是一个基于 `FBV` 的用户登录应用 `account`

要实现视图功能需要一下步骤：
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

def login(request):
    # post 请求的业务逻辑，只有在提交表达时才会触发
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 登陆业务逻辑，验证用户 ｜ 密码是否在数据库中等，这里模拟登陆成功的逻辑
        return HttpResponse(f'login success with {username} and password {password}')
    # 默认是 GET() 请求，渲染 login.html
    return render(request, 'login.html')

```