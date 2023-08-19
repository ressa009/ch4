from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

def news_list(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    news_list = News.objects.all().order_by('-news_date')

    if kw:
        post_list = news_list.filter(
            Q(news_title_title__icontains=kw) # 제목 검색
        ).distinct()

    paginator = Paginator(news_list, 10)
    try: page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.get_page(page)

    leftIndex = (int(page) - 2)
    rightIndex = (int(page) + 2)

    if leftIndex < 1:
        leftIndex = 1

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)


    return render(request, 'news/news.html', {'news_list': news_list,
                                               'page_obj': page_obj,
                                               'paginator': paginator,
                                               'custom_range': custom_range,
                                               'page' : page,
                                               'kw': kw})