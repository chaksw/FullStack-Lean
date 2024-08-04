# Django + Vue Course
> 这个 README.md 作为 Django/LEARN/Django 课程的进阶延伸.

## 路由匹配模式 （`urls.py` 中的url路径定义方式）
1. 字符串精准匹配： 定义啥就识别啥
```python
# urls.py
path('hello/', helloWorld), # 只识别 'hello' or 'hello/' 地址
# name 的定义让我们可以在 template中通过name来访问该路由
path('acticle/create/', article_create, name='article_create'),  # 只识别 article/create地址
```
2. 路径转换器格式 `<type:value>` 一般用于访问符合特定属性的属性
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
3. 正则表达式：`re_path` 用于验证 `url` 是否满足特定字符匹配规则
```python
# 1. ^: 以什么开始，精准匹配字符
# 2. (?P<phone_number> 1[3456789]\d{9}) 一个捕获组，名字为phone_number， 必须以数字 1 开头， 第二位必须是 3、4、5、6、7、8 或 9 中的一个数字。 接下来的 9 位必须是数字 (0-9)
# 3. /$: 以 '/' 结尾
re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', phone_detail, name='phone_detail'),
```