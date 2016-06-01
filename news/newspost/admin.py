from django.contrib import admin

from models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(NewsPost, NewsPostAdmin)
