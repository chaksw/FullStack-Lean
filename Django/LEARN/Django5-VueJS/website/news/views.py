from django.shortcuts import render
from django.http import HttpResponse
from news.models import News, Category
# Create your views here.


def new_list(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request=request, template_name='list.html', context=context)


def detail(request, id):
    try:
        news = News.objects.get(pk=id)
        context = {
            'news': news,
        }
        return render(request, 'detail.html', context)
    except:
        return render(request, '404.html')
