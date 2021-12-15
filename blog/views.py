from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, post_id=post_pk, pk=post_pk)
    return render(request, 'blog/post_detail.html', {'post': post})
