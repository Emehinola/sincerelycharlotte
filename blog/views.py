from django.shortcuts import render, redirect
from . models import Blog, Comment, Like, DailyThought
from . forms import CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    pass

def index(request):
    posts = Blog.objects.all()
    thought = None
    likes = None
    try:
        likes = Like.objects.filter(author=request.user) # getting blog post likes
        thought = DailyThought.objects.all()[0]
    except:
        pass
    
    hot = Blog.objects.all()[:3]
    context = {
        'title': 'Home',
        'blogs': posts,
        'likes': likes,
        'thought': thought,
        'hot': hot
    }
    return render(request, 'blog/home.html', context)

def single_blog(request, id):
    post = Blog.objects.get(id=id) # a single post
    comments = Comment.objects.filter(post_id=id)  # getting comments on the post
    thought = None
    hot = Blog.objects.all()[:3]
    posts = Blog.objects.all()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = id
            try:
                if request.user == "AnonymousUser":
                    comment.userEmail = request.userEmail
                else:
                    comment.author = request.user
                    
            except:
                pass
            comment.save()
            form = CommentForm()
            return redirect(f'/posts/{id}')

    else:
        try:
            thought = DailyThought.objects.all()[0]
        except:
            pass
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'thought': thought,
        'hot': hot,
        'blogs': posts,
        'title': post.title
    }
    return render(request, 'blog/single-blog.html', context)

@login_required
def like(request):
    action = request.GET.get('action')
    post_id = request.GET.get('post_id')
    post = Blog.objects.get(id=post_id)

    if action == 'like':
        like_post, created = Like.objects.get_or_create(author=request.user, post=post, liked = True)
        like_post.save()

    elif action == 'unlike':
        like = Like.objects.filter(author=request.user, post=post)
        like.delete()
    data = {
        'action': action
    }

    return JsonResponse(data, safe=False)

def get_like(request):
    post_id = request.GET.get('post_id')
    check_status = None
    try:
        check_status = Like.objects.filter(author=request.user, post_id=post_id).exists()
    except:
        pass
    number_of_likes = Like.objects.filter(post_id=post_id).count()
    
    data = {
        'liked': check_status,
        'number': number_of_likes
    }
    return JsonResponse(data, safe=False)

def category(request, category):
    hot = Blog.objects.all()[:3]
    posts = Blog.objects.filter(category=category)
    blogs = Blog.objects.all()
    thought = None
    likes = None
    
    try:
        likes = Like.objects.filter(author=request.user)
        thought = DailyThought.objects.all()[0]
    except:
        pass

    context = {
        'title': category,
        'posts': posts,
        'likes': likes,
        'blogs': blogs,
        'thought': thought,
        'hot': hot
    }

    return render(request, 'blog/same-category.html', context)