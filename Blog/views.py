from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BlogForm
from .models import Blog

def dashborad(request):
    return render(request, 'blog/dashboard.html')


def create_blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/blog_list')  
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})



def update_blog_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog/blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update_blog.html', {'form': form})


def delete_blog_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog/blog_list')
    return render(request, 'blog/delete_blog.html', {'blog': blog})


def list_blogs_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


