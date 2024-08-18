from django.shortcuts import render
from django.http import HttpResponse
from slide.models import Slide
from team.models import Team
# Create your views here.


def index(request):
    # get all slide data
    slides = Slide.objects.all()
    # get all team data
    # 使用 order_by 进行基于 rank 字段的排序
    # teams = Team.objects.all().order_by('rank')
    # 倒序
    teams = Team.objects.all().order_by('-rank')
    # {'slides': slides} 中 'slides' 为可供模版调用的变量， slides 为实际数据
    return render(request, 'index.html', context={'slides': slides, 'teams': teams})
