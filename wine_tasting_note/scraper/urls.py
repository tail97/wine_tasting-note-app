from django.contrib import admin
from django.urls import path
from . import views
from . views import TastingListView

app_name = 'scraper' 
urlpatterns = [
    #웹 홈페이지 url연동
    # path('admin/', admin.site.urls),//
    path('whitewine/', views.White, name= 'white' ),
    path('redwine/', views.Red, name= 'red' ),
    path('rosewine/', views.Rose, name= 'rose' ),
    path('tastingnote/', TastingListView.as_view(), name= 'tastingnote' ),
]