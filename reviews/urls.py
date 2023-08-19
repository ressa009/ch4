from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('',  views.review_list, name='review_list'),
    path('detail/<int:rev_com_id>/',  views.review_detail, name='review_detail'),
]