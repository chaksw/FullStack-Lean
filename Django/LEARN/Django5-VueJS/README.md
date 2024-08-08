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

### CBV - Class-Based View
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

### `FBV` & `CBV` 区别
**`FBV` 对于基于HTTP协议的交互方法的业务逻辑是通过判断 `request` 的 `http` 方法来展开的，这不利于复杂的业务逻辑，而 `CBV` 继承于 `django` 的 `View`， `View` 作为父类包含了基于 `HTTP` 协议的交互方法, 这些方法对应不同的数据处理场景自动运行，我们只需要关注它们的业务逻辑实现。**

### `HttpRequest` & `HttpResponse` 的一些内容
#### `HttpRequest` 
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

#### `HttpResponse`
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

## `Tempaltes` 模版
1. 关于模版引擎和配置关注 `settings.py` 中的 `INSTALLED_APP` 和 `TEMPLATES`
2. 关于模版的语法知识和继承可以在 `LEARN/Django/README.md` 的 Section 1.2. Template and Django template language 中了解 
3. 关于 `{% include '*.html'%}` 的用法后续用到后再补充，简单来说就是将一个简单的组件式 `html` 通过 `include` 引入到别的 `html` 中