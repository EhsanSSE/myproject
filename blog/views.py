from django.shortcuts import render
from blog.models import Post
from django.utils.timezone import now
from django.shortcuts import get_object_or_404


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=now())
    context = {'posts': posts}
    return render(request, 'blog/blog-3.html', context)

def blog_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True, published_date__lte=now())
    context = {'post': post}
    return render(request, 'blog/blog-details.html', context)