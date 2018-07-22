from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


# 首页
def index(request):
    return render(request, 'index.html')


# 联系
def contact(request):
    return render(request, 'contact.html')


# 博客s
def blogs(request):
    post_list = Post.objects.all()
    return render(request, 'blogs.html', context={'post_list': post_list})


# 博客s-归档
def blogs_archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blogs.html', context={'post_list': post_list})


# 博客s-分类
def blogs_category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blogs.html', context={'post_list': post_list})


# 博客s-标签
def blogs_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag)
    return render(request, 'blogs.html', context={'post_list': post_list})


# 博客s-标签
def blogs_search(request, word):
    post_list = Post.objects.filter(title=word)
    return render(request, 'blogs.html', context={'post_list': post_list})



# 博客-单文章详细页
def blog(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    # markdow解析为html
    # import markdown
    # from markdown.extensions.toc import TocExtension
    # from django.utils.text import slugify
    # md = markdown.Markdown(extensions=[
    #     'markdown.extensions.extra',  # 代码块
    #     'markdown.extensions.codehilite',  # 代码高亮
    #     'markdown.extensions.toc',  # 目录
    #     'markdown.extensions.tables',  # 表格
    #     TocExtension(slugify=slugify),
    # ])
    # post.body = md.convert(post.body)
    # post.toc = md.toc

    return render(request, 'blog.html', context={'post': post})
