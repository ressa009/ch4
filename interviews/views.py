from django.shortcuts import render
from .models import Interview
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

def interview_list(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    interview_list = Interview.objects.all().order_by('-int_date')

    if kw:
        interview_list = interview_list.filter(
            Q(name_list__icontains=kw) |  # 제목 검색
            Q(int_result__icontains=kw)  # 내용 검색
        ).distinct()

    paginator = Paginator(interview_list, 10)
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



    return render(request, 'interviews/interview.html', {'interview_list': interview_list,
                                                         'page_obj': page_obj,
                                                         'paginator': paginator,
                                                         'custom_range': custom_range,
                                                         'page' : page,
                                                         'kw': kw})



def interview_detail(request, name_list):

    interview_com_list = Interview.objects.filter(name_list=name_list)
    interview_1 = interview_com_list[0]
    return render(request, 'interviews/interview_detail.html', {'interview': interview_com_list, 'interview_1': interview_1})