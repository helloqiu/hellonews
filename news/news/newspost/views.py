from django.shortcuts import render_to_response, get_object_or_404
from models import NewsPost, NewsColumn


def index(request):
    return render_to_response('index.html', {
        'posts': NewsPost.objects.all()[:5],
        'columns': NewsColumn.objects.all(),
    })


def view_post(request, **kwargs):
    return render_to_response('news_view.html', {
        'post': get_object_or_404(NewsPost, slug=kwargs['slug'])
    })
