from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Grade
from .forms import GradeForm
# Create your views here.


class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grades_list.html'
    fields = ['grade_name', 'grade_number']
    # 表示使用 render() 函数是，传递到模版的参数
    # 等效为: render(request=request, context=grades)
    context_object_name = 'grades'
    '''
    实现分页功能
    定义每页显示记录数量
    ListView 在定义了 paginate_by 后，会自动将 page_obj 对象传递到对应的 template 中
    page_obj.number 显示当前页码
    page_obj.paginator.num_pages 总页数
    page_obj.paginator.count paginator 对象总数
    page_obj.paginator.page_range 所有页面的页码
    page_obj.has_next() 检查是否有下一页
    page_obj.next_page_number() 获取下一页页码的URL
    page_obj.has_previous() 检查是否有上一页
    page_obj.previous_page_number() 获取上一页页码的URL
    ...
    '''

    paginate_by = 10

    # 通过重写 MultipleObjectMixin <- BaseListView 中的 get_queryset() 实现搜索功能

    def get_queryset(self):
        queryset = super().get_queryset()
        # 获取搜索的关键词：
        # 1. 表单为 GET 请求 所以数据存储在 request.GET 下
        # 2. 数据来源于 input 元素下 attribute name='search' 的内容，所以在 request.GET 下获取  'search' 的内容
        search = self.request.GET.get('search')
        if search:
            query = Q(grade_name__icontains=search) | Q(grade_number__icontains=search)
            queryset = queryset.filter(query)
        return queryset


# 结合 表单类创建 新增表单
class GradeCreateView(CreateView):
    model = Grade
    # 创建数据需要定义表单类
    form_class = GradeForm
    template_name = 'grades/grade_form.html'
    # 当 type='sumbit' 的按钮按下后，会提交表单，产生一个 post 请求，将表单数据发送到服务器
    # 服务器接收到数据后，CreateView 会调用 form.is_valid() 方法来验证数据是否合法
    # 如果数据有效，会自动调用 form.save() 将数据保存到数据库中
    # 如果数据保存，会重定向到 success_url 中指定的页面
    success_url = reverse_lazy('grades_list')


# 更新视图和创建视图基本相同，，因为都是处理同个数据模型的表单的 POST 请求，（更新也可以是 PUT 请求，但是 django CBV 不直接支持 PUT 请求，但可以使用 Django REST Framework 来实现）。
# 区别在于，更新视图是更新已有数据，可以在更新页面中需要接受和显示对应的数据，接受数据在编辑按钮中的 url 添加对应的pk来实现，而显示对应数据则是 form 表单中的 {{ field }}
class GradeUpdateView(UpdateView):
    model = Grade
    # 创建数据需要定义表单类
    form_class = GradeForm
    template_name = 'grades/grade_form.html'
    success_url = reverse_lazy('grades_list')


# 删除视图比新增/更新很类似，他们都是以处理表单数据，同样是发送 post 请求，跟更新数据一样需要接受对应的数据，因为不需要对数据进行编辑或者新建，所以不需要输入框。
class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/grade_delete_confirm.html'
    success_url = reverse_lazy('grades_list')
