from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-3.html')

def blog_details_view(request):
    return render(request, 'blog/blog-details.html')