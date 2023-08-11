from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

urlpatterns = [
    # URL pattern for displaying a list of posts
    path('', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],  # Queryset to retrieve and order posts by date
        template_name="blog.html"  # Template to render the list of posts
    )),

    # URL pattern for displaying a single post
    path(
        '<int:pk>/',  # URL pattern to capture the primary key  of the post
        DetailView.as_view(
            model=Post,  # Model class to retrieve the post
            template_name="post.html"  # Template to render the single post
        )
    ),
]
