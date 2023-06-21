from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Blog,Category
from .forms import BlogForm
from .utils import check_emotion

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# name = request.GET.get('full_name')
    # address = request.GET.get('address')
    # context = {
    #     'response': "{} is from {}".format(name,address),
    #     'sent':"this-is-normal"
    # }
from django.contrib.auth import login,authenticate,logout

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect('blog:blog_index')
        else:
            messages.error(request,"Username or Password Error")

    return render(request,'login.html',{})



@login_required(login_url="blog:loginPage")
def blog_index(request):
        
    query = request.GET.get('query')
    if query is not None and query != '':
        blogs = Blog.objects.filter(title__icontains=query).order_by('-id')
    else:
        blogs = Blog.objects.all().order_by('-id')
    # print(request.GET)
    # print("value is persent")
    # query = request.GET['query']
    
    context = {
        'page_title':"BLOG LISTING",
        'blogs':blogs
    }
    return render(request,'blog/list.html',context)



@login_required(login_url="blog:loginPage")
def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():

            title_data = form.cleaned_data.get('title')
            emotion = check_emotion(title_data)
            print(emotion)
            if emotion == "POSITIVE":
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()

                messages.success(request,"Blog Created")
                # messages.success(request,"successfully created")
                return redirect('blog:blog_index')
            
            else:
                messages.success(request,"the title is negative please improve your words")
            print("form valid")
            # save the form which ultimately creates object in database
            
            
    context = {
        "page_title":"BLOG CREATE",
        'form':form
    }
    return render(request,'blog/create.html',context)



@login_required(login_url="blog:loginPage")
def blog_edit(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    # blog = get_object_or_404(Blog,id=id)
    form = BlogForm(instance=blog)
    #TODO:
    ## form handling
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance = blog)
        if form.is_valid():
            print("form valid")
            # save the form which ultimately updates the object
            form.save()
            return redirect('blog:blog_index')
    context = {
        'blog':blog,
        'form':form,
    }
    return render(request,'blog/edit.html',context)



@login_required(login_url="blog:loginPage")
def blog_delete(request,id):
    blog = get_object_or_404(Blog,id=id)
    if request.method == 'POST':
        blog.delete()
        messages.error(request,"Blog Deleted")
        return redirect('blog:blog_index') # return to blog list view
    context = {
        'blog':blog
    }
    return render(request,'blog/confirm-delete.html',context)
    


@login_required(login_url="blog:loginPage")
def blog_view(request):
    blogs = Blog.objects.filter
    total_blogs = Blog.objects.all().count()
    draft_blogs = Blog.objects.filter(status='draft').count()
    context = {
        'blogs':blogs,
        'total_blogs':total_blogs,
        'draft_blogs':draft_blogs,
    }
    return render(request,'blog/list.html',context)


def data_view(request,data):
    print(data)
    context ={
        'data':data
        
    }
    return render(request,'blog/test.html',context)

def test_redirect(request):
    google_url = "https://google.com"
    return redirect(google_url)
