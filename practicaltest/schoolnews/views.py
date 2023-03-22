from django.shortcuts import render
from schoolnews.models import News

def index(request):
    news_list = News.objects
    context_dict = {}
    context_dict['boldmessage'] = 'Read all about it!'
    context_dict['news'] = news_list
    return render(request, 'schoolnews/index.html', context=context_dict)

