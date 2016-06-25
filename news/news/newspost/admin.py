#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

from models import NewsPost, NewsColumn


class NewsPostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class NewsColumnAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(NewsColumn, NewsColumnAdmin)
