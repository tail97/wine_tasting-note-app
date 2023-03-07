from django.shortcuts import render
# from django.views.generic import ListView
from .models import White_wine , Wine
from django.core.paginator import Paginator
import math

# 웹 홈페이지 구현 
def index(request):
    wine = Wine.objects.all().order_by("-cdate")
    return render(request, "index.html", {'wine':wine})

def White(request):
    whitewine = White_wine.objects.all().order_by("-cdate")
    
    page = request.GET.get('page')
    paginator = Paginator(whitewine,6)
    page_obj = paginator.get_page(page)
    page_range = 5 #페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
    current_block = math.ceil(int(page)/page_range) #해당 페이지가 몇번째 블럭인가
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    

    return render(request, 'white_wine_list.html',{'whitewine':whitewine, 'whitewine':page_obj , 'p_range':p_range})