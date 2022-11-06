from django.shortcuts import render
from .models import Category, Comment, Post
from django.shortcuts import render, redirect
from .forms import CommentForm
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')
    categorys = Category.objects.filter(post=post)
    related = Post.objects.filter(category=post.category.all()[0])
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.save()
            return redirect(f'/detail/{slug}')
    else:
        form = CommentForm()
    context = {
        'object': post,
        'form': form,
        'comments': comments,
        'categorys': categorys,
        'related': related
    }
    return render(request, 'post.html', context)
