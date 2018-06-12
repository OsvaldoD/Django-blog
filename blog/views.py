from django.shortcuts import render
from .models import Post, Autor

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-data')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)