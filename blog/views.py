from django.shortcuts import render
from .models import Post, Autor

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-data')
    body = ''
    
    for post in posts:
        body = post.corpo[:250]
        moment = str(post.data)
    data = moment.split(' ')[0]
    context = {'posts': posts,'corpo':body, 'data':data}
    return render(request, 'blog/index.html', context)

def detail(request, question_id):
    post = Post.objects.get(pk=question_id)
    context = {'id':post}
    return render(request, 'blog/detail.html',context)