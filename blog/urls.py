from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pk>', blog_details_view, name='details'),
    path('category/<str:category>', blog_view, name='category'),
    path('author/<str:author>', blog_view, name='author'),
    path('search/', blog_search_view, name='search')
]
