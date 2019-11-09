from django.shortcuts import render

from blog.models import Blog
# Create your views here.
def blog_Page(request):
    # 查询集
    blogs = Blog.objects.all()
    print (type(blogs))
    return render(request,'blog.html',{'blogs':blogs})