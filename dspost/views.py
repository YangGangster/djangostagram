from django.shortcuts import render
from django.views.generic import ListView

from dspost.models import Post

class PostListView(ListView):
    template_name = 'post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.all().order_by('-registered_date')
