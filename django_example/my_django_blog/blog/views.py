from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-create_at')
    return render(request, 'index.html', {'posts': posts})