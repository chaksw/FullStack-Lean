from django import template
from django.http import QueryDict
from urllib.parse import urlencode

# 创建自定义模版标签
# 创建一个 url加入到分页跳转的url中，让分页跳转时基于当前的url所对应的视图进行分页跳转
register = template.Library()


@register.simple_tag
def search_url(request, **kwargs):
    query_params = QueryDict(request.META['QUERY_STRING'], mutable=True)
    for key, value in kwargs.items():
        if value is None:
            query_params.pop(key, None)
        else:
            query_params.setlist(key, [value])
    return urlencode(query_params, doseq=True)
