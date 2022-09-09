from django import template
from BlogApp.models import Post
register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts() :
    return Post.objects.count()

@register.inclusion_tag('BlogApp/latest_post.html')
def show_latest_post(count=3) :
    latest_post=Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}
from django.db.models import Count

@register.simple_tag
def get_most_commented_posts(count=5) :
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments') [:count]