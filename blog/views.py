from django.shortcuts import render,redirect
from .models import BlogPost,Comment
from .forms import BlogPostForm
# Create your views here.
def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts':posts})

def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('blog:blogs')  
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


def blogs_comments(request, id):
    post = BlogPost.objects.get(id = id)
    return render(request, "blog_comments.html", {'post':post}) 

def blog_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments}) 
