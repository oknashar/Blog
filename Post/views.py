from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

def all_post(request):
    all_posts= Post.objects.all()
    context = {
        'all_posts':all_posts,
    }
    return render(request,'allposts.html',context)



def post(request , id):
    #post=Post.objects.get(id=id)
    post = get_object_or_404(Post,id=id)
    context= {
        'post' : post
    }
    return render(request , "post.html",context)