from django.shortcuts import render
from django.http import HttpResponse
from slide.models import Slide
from team.models import Team
from news.models import News, Category

# Create your views here.


def index(request):
    # get all slide data
    slides = Slide.objects.all()
    # get all team data
    # 使用 order_by 进行基于 rank 字段的排序
    # teams = Team.objects.all().order_by('rank')
    # 倒序
    teams = Team.objects.all().order_by('-rank')
    # 获取新闻数据，只获取 category 为新闻 (对应category id=6), 并以创建时间倒序排序，且限制数量为3个
    news = News.objects.filter(category__id=6).order_by('-created_at')[:3]
    # 获取成功案例：除了 category 为 新闻以为的 news 数据, 使用 filter().exclude
    cases = News.objects.filter().exclude(category__id=6).order_by('-created_at')[:6]
    context = {
        'slides': slides,
        'teams': teams,
        'news': news,
        'cases': cases,
    }
    # {'slides': slides} 中 'slides' 为可供模版调用的变量， slides 为实际数据
    return render(request, 'index.html', context=context)
