from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone
# Create your views here.
def hello(request):
    return render(request, "hello.html")

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = Blog.objects.get(id = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.name = request.GET['name']
    blog.idnum = request.GET['idnum']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    Blog.objects.get(id = blog_id).delete()
    return redirect('/')

def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.title = request.POST.get('title')
    blog.name = request.POST.get('name')
    blog.idnum = request.POST.get('idnum')
    blog.pub_date = timezone.datetime.now()
    blog.body = request.POST.get('body')
    blog.save()
    return redirect('/blog/' + str(blog.id))
    
def aboutme(request):
    return render(request, "aboutme.html")