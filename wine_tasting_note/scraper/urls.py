from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #웹 홈페이지 url연동
    # path('admin/', admin.site.urls),//
    path('whitewine/', views.White, name= 'white' ),
]