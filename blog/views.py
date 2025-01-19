from django.shortcuts import render
from blog.models import Post
from django.utils.timezone import now
from django.shortcuts import get_object_or_404


# Create your views here.
def blog_view(request, category=None, author=None):
    filters = {'status': True, 'published_date__lte': now()}
    if category:
        filters['category__name'] = category
    elif author:
        filters['author__first_name'] = author

    posts = Post.objects.filter(**filters)
    context = {'posts': posts}
    return render(request, 'blog/blog-3.html', context)

def blog_details_view(request, pk):
    posts = Post.objects.filter(status=True, published_date__lte=now())
    post = get_object_or_404(posts, pk=pk)
    post.counted_views += 1
    post.save()
    posts_list = list(posts)
    index_post = posts_list.index(post)
    previous_post = posts_list[index_post - 1] if index_post > 0 else None
    next_post = posts_list[index_post + 1] if index_post < len(posts_list) -1 else None
    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blog-details.html', context)

def blog_search_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-3.html', context)