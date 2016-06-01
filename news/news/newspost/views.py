from django.shortcuts import render, render_to_response, get_object_or_404
from models import NewsPost


def index(request):
    return render_to_response('index.html', {
        'posts': NewsPost.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('news_post_detail.html', {
        'post': get_object_or_404(NewsPost, slug=slug)
    })
