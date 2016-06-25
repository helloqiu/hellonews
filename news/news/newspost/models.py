from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink


class NewsColumn(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '%s' % self.title


class NewsPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    column = models.ForeignKey(NewsColumn, null=False, default='default')
    author = models.CharField(max_length=100, unique=False)
    slug = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_news_post', None, {'slug': self.slug}
