from django.shortcuts import render
from .models import Post, Autor

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-data')
    body = ''
    for post in posts:
        body = post.corpo[:350]
    context = {'posts': posts,'corpo':body}
    return render(request, 'blog/index.html', context)
