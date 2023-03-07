from django.shortcuts import render
# from django.views.generic import ListView
from .models import White_wine , Wine

# 웹 홈페이지 구현 
def index(request):
    wine = Wine.objects.all().order_by("-cdate")
    return render(request, "index.html", {'wine':wine})

def White(request):
    whitewine = White_wine.objects.all().order_by("-cdate")
    return render(request, 'white_wine_list.html',{'whitewine':whitewine})