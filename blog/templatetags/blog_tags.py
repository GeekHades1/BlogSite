from django import template
from django.db.models.aggregates import Count
from django.utils import timezone

from blog.models import Post, Category, Tag, ShareWeb, OfferLink

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    posts = Post.objects.all()[:num]
    return posts


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_friendly():
    return ShareWeb.objects.all()

@register.simple_tag
def get_offer_link():
    return OfferLink.objects.all()