from django.contrib import admin

from scraper.models import Wine,White_wine,Rose_Wine ,Tastingnote
# 장고 admin페이지에 와인데이터 저장 
admin.site.register(Wine)
admin.site.register(White_wine)
admin.site.register(Rose_Wine)
admin.site.register(Tastingnote)
