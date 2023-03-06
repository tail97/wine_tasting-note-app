from django.shortcuts import render
from .models import Wine

# 웹 홈페이지 구현 
def index(request):
    wine = Wine.objects.all().order_by("-cdate")
    return render(request, "index.html", {'wine':wine})
