from django.shortcuts import render,redirect
from .models import *
from .forms import *
from blog.models import BlogPost,Comment
from blog.forms import BlogPostForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 
# Create your views here.
def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, "home/index.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    view class to create post
    """
    model = Post
    fields = "__all__"
    template_name = 'hoods/create_hood.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required(login_url='/accounts/login/')
def post(request, pk):
    """
    View to handle post model
    Args:
    Pk - Primary Key,an unique way to identify an object uniquely in relational database systems
    """

    post = Post.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author= user,description=form.cleaned_data["description"],post=post)
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-date_posted')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
   
    return self.get(self, request, pk, context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'hoods/hood.html'
    context_object_name = 'post'

def joinHood(request,pk):
    hood =  Post.objects.get(id=pk)
    hood.occupants.add(request.user)
    occupants = hood.occupants.all()

    context = {
       'hood':hood,
       'occupants':occupants 
    }
    return render(request, 'hoods/hood.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = BlogPost.objects.get(id=pk)

    if request.user != post.author:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        post.delete()
        return redirect('homepage:index')
    context = {

    }
    return render(request, 'hoods/delete.html', {'obj':post})


@login_required(login_url='login')
def createBusiness(request, pk):
    hood = Post.objects.get(id=pk)
    form = BusinessForm()
    user = request.user

    if request.method == 'POST':
        business = Business.objects.create (
            owner = user,
            neighborhood = hood,
            name = request.POST.get('name'),
            email= request.POST.get('email'),
            phone = request.POST.get('phone'),

        )
        return redirect('homepage:post-detail', pk=hood.id)     
    context = {
        'form':form,
        'hood': hood
    }
    return render(request, 'hoods/create_bussiness.html', context)

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any  category"
    return render(request, 'results.html', {'message': message})