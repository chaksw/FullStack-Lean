from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Grade

# Create your views here.


class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grades_list.html'
    fields = ['grade_name', 'grade_number']
    # 表示使用 render() 函数是，传递到模版的参数
    # 等效为: render(request=request, context=grades)
    context_object_name = 'grades'

    # 实现分页功能
    # 定义每页显示记录数量
    # ListView 在定义了 paginate_by 后，会自动将 page_obj 对象传递到对应的 template 中
    # page_obj.number 显示当前页码
    # page_obj.paginator.num_pages 总页数
    # page_obj.paginator.count paginator 对象总数
    # page_obj.paginator.page_range 所有页面的页码
    # page_obj.has_next() 检查是否有下一页
    # page_obj.next_page_number() 获取下一页页码的URL
    # page_obj.has_previous() 检查是否有上一页
    # page_obj.previous_page_number() 获取上一页页码的URL
    # ...
    paginate_by = 10

    # 通过重写 MultipleObjectMixin <- BaseListView 中的 get_queryset() 实现搜索功能

    def get_queryset(self):
        queryset = super().get_queryset()
        # 获取搜索的关键词：
        # 1. 表单为 GET 请求 所以数据存储在 request.GET 下
        # 2. 数据来源于 text 元素下 attribute name='search' 的内容，所以在 request.GET 下获取  'search' 的内容
        search = self.request.GET.get('search')
        if search:
            query = Q(grade_name__icontains=search) | Q(grade_number__icontains=search)
            queryset = queryset.filter(query)
        return queryset
