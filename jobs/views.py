from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import redirect
# Create your views here.

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    post_list = Post.objects.all().order_by('post_id')

    if kw:
        post_list = post_list.filter(
            Q(post_title__icontains=kw) |  # 제목 검색
            Q(post_com_name__icontains=kw)  # 내용 검색
        ).distinct()

    paginator = Paginator(post_list, 10)
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



    return render(request, 'jobs/index.html', {'post_list': post_list,
                                               'page_obj': page_obj,
                                               'paginator': paginator,
                                               'custom_range': custom_range,
                                               'page' : page,
                                               'kw': kw})




















