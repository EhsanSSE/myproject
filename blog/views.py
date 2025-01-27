from django.shortcuts import render, redirect
from blog.models import Post, Comment
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm


# Create your views here.
def blog_view(request, category=None, author=None, tag_slug=None):
    filters = {'status': True, 'published_date__lte': now()}
    if category:
        filters['category__name'] = category
    elif author:
        filters['author__first_name'] = author
    elif tag_slug:
        filters['tags__slug'] = tag_slug

    posts = Post.objects.filter(**filters)
    
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-3.html', context)

def blog_details_view(request, pk):
    posts = Post.objects.filter(status=True, published_date__lte=now())
    post = get_object_or_404(posts, pk=pk)
    post.counted_views += 1
    post.save()

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:details', pk=pk)
    else:
        form = CommentForm()

    comments = Comment.objects.filter(active=True, parent__isnull=True, post=post.id)       
    posts_list = list(posts)
    index_post = posts_list.index(post)
    previous_post = posts_list[index_post - 1] if index_post > 0 else None
    next_post = posts_list[index_post + 1] if index_post < len(posts_list) -1 else None
    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post, 'comments': comments, 'form': form}
    return render(request, 'blog/blog-details.html', context)

def blog_search_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-3.html', context)