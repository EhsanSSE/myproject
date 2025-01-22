from django import template
from blog.models import Post
from django.utils.timezone import now


register = template.Library()


@register.inclusion_tag('main/blog-latestpost.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=True, published_date__lte=now()).order_by('-published_date')[:arg]
    return {'posts': posts}