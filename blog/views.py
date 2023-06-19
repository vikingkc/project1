from django.shortcuts import render
from .models import Blog,Category
# Create your views here.

# name = request.GET.get('full_name')
    # address = request.GET.get('address')
    # context = {
    #     'response': "{} is from {}".format(name,address),
    #     'sent':"this-is-normal"
    # }
def blog_view(request):
    blogs = Blog.objects.filter(status='published')
    total_blogs = Blog.objects.all().count()
    draft_blogs = Blog.object.filter(status='draft').count()
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
