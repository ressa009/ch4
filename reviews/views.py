from django.shortcuts import render
from .models import Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def review_list(request):

    review_list = Review.objects.all().order_by('-rev_com_name')
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어

    if kw:
        review_list = review_list.filter(
            Q(rev_title__icontains=kw) |  # 제목 검색
            Q(rev_com_name__icontains=kw)  # 회사명 검색
        ).distinct()

    paginator = Paginator(review_list, 10)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 2)
    rightIndex = (int(page) + 2)

    if leftIndex < 1:
        leftIndex = 1

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    return render(request, 'reviews/review.html', {
                                                'review_list': review_list,
                                                'page_obj': page_obj,
                                                'paginator': paginator,
                                                'custom_range': custom_range,
                                                'page': page,
                                                'kw': kw})



def review_detail(request, rev_com_id):
    review_com_list = Review.objects.filter(rev_com_id=rev_com_id)
    review_1 = review_com_list[0]
    return render(request, 'reviews/review_detail.html', {'review': review_com_list, 'review_1': review_1})