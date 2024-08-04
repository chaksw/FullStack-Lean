from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloWorld(request):
    return HttpResponse('Hello World !')


def article_create(request):
    return HttpResponse('create an article')


def article_detail(request, article_id, title):
    return HttpResponse(f'ID of article detail: {article_id}, title: {title}')


def phone_detail(request, phone_number):
    return HttpResponse(f'phone number: {phone_number}')
