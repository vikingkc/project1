from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Blog,Category
from .forms import BlogForm
# Create your views here.

# name = request.GET.get('full_name')
    # address = request.GET.get('address')
    # context = {
    #     'response': "{} is from {}".format(name,address),
    #     'sent':"this-is-normal"
    # }
def blog_index(request):
        
    query = request.GET.get('query')
    if query is not None:
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.all()
    # print(request.GET)
    # print("value is persent")
    # query = request.GET['query']
    
    context = {
        'page_title':"BLOG LISTING",
        'blogs':blogs
    }
    return render(request,'blog/list.html',context)

def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            print("form valid")
            # save the form which ultimately creates object in database
            form.save()
            return redirect('blog:blog_view')
    context = {
        "page_title":"BLOG CREATE",
        'form':form
    }
    return render(request,'blog/create.html',context)

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
        form = BlogForm(request.POST,instance = blog)
        if form.is_valid():
            print("form valid")
            # save the form which ultimately updates the object
            form.save()
            return redirect('blog:blog_view')
    context = {
        'blog':blog,
        'form':form,
    }
    return render(request,'blog/edit.html',context)


def blog_delete(request,id):
    blog = get_object_or_404(Blog,id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog:blog_view') # return to blog list view
    context = {
        'blog':blog
    }
    return render(request,'blog/confirm-delete.html',context)
    

def blog_view(request):
    blogs = Blog.objects.filter(status='published')
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
