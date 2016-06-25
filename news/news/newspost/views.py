#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import NewsPost, NewsColumn


def index(request):
    column = request.GET.get("column", None)
    if column is not None:
        column = get_object_or_404(NewsColumn, title=column)
        return render_to_response('index.html', {
            'posts': get_list_or_404(NewsPost, column=column),
            'columns': NewsColumn.objects.all(),
            'index': True,
        })
    return render_to_response('index.html', {
        'posts': NewsPost.objects.all(),
        'columns': NewsColumn.objects.all(),
        'index': True,
    })


def view_post(request, **kwargs):
    return render_to_response('news_view.html', {
        'post': get_object_or_404(NewsPost, slug=kwargs['slug']),
        'view': True,
    })
