from django import template
from blog.models import Post, Category
from django.utils.timezone import now


register = template.Library()


@register.inclusion_tag('blog/blog-latest-post.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=True, published_date__lte=now()).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-categories.html')  
def postcategories():
    posts = Post.objects.filter(status=True, published_date__lte=now())
    categories = Category.objects.all()
    cat_dic ={}
    for name in categories:
        cat_dic[name]=posts.filter(category=name).count()
    return {'categories': cat_dic}