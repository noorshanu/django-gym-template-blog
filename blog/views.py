from django.shortcuts import render

from .models import Blog
# Create your views here.
def home(request):
    myposts = Blog.objects.all()

    return render(request, 'blog/index.html', {'myposts':myposts})

def blogpost(request, id):
    post = Blog.objects.filter(post_id=id)[0]
    print(post)


    return render(request, 'blog/blogpost.html',{'post':post})
