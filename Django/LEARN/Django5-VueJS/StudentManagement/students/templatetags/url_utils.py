from django import template
from django.http import QueryDict
from urllib.parse import urlencode

# 创建自定义模版标签
# 创建一个 url加入到分页跳转的url中，让分页跳转时基于当前的url所对应的视图进行分页跳转
register = template.Library()


# 注册自定义模板标签，允许在模板中直接使用该函数
@register.simple_tag
def search_url(request, **kwargs):
    # QueryDict 用于处理 reqeust 中查询字符串中的参数（GET 请求中的数据）。它支持多个值的参数，比如 ?filter=price&filter=category
    # request.META 是包含 HTTP 请求的元数据的字典
    # request.META['QUERY_STRING'] 是从请求对象中提取的查询字符串部分，类似于 URL 中的 ?key=value&another_key=value 这样的部分
    # mutable=True 参数允许对这个 QueryDict 进行修改
    # 总的来说就是从请求对象中提取查询字符串的部分，并将其解析为一个字典形式，如： filter=price&filter=category 转化为 {'filter': ['price', 'category']}
    query_params = QueryDict(request.META['QUERY_STRING'], mutable=True)
    for key, value in kwargs.items():
        if value is None:
            query_params.pop(key, None)  # 如果值为 None (如：若?filter=&filter=category，中第一个的value为 None)，删除对应的查询参数
        else:
            # 添加新的参数值，如 kwargs 中传入为 page=2，原始request经过QueryDict转化为 query_param={'filter': ['price', 'category']}, 则经过该处理后 query_params={'filter': ['price', 'category'], 'page': ['2']}
            query_params.setlist(key, [value])
    # urlencode 将更新后的 query_params（QueryDict 对象）编码成 URL 格式的查询字符串： 如 query_params={'filter': ['price', 'category'], 'page': ['2']} 经过转化变为 filter=price&filter=category&page=2
    # doseq=True 表示如果有多个值的键（比如 filter': ['price', 'category'] 转化为 filter=price&filter=category），它会为每个值分别生成键值对，而不是合并为单个值。
    return urlencode(query_params, doseq=True)
