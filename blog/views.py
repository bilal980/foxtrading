from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages


def foxBlog(request):
    if request.user.is_authenticated:
        total = Post.objects.all().count()
        allpost = Post.objects.all().order_by('-time')
        context = {'allpost': allpost, 'total': total, 'sbar': 'blog'}
        return render(request, 'blog/blog.html', context)
    else:
        messages.error(request, 'Please Login To Continue')
        return redirect("/")


def foxdetailpost(request, slug):
    if request.user.is_authenticated:
        postdetail = Post.objects.filter(slug=slug).first()
        comments = BlogComment.objects.filter(
            post=postdetail).order_by('time')
        totalcomment = BlogComment.objects.filter(post=postdetail).count()
        context = {'postdetail': postdetail, 'comments':
                   comments, 'totalcomment': totalcomment,
                   }
        return render(request, 'blog/detailpost.html', context)
    else:
        messages.error(request, 'Please Login To Continue')
        return redirect("/")


def comment_post(request):
    if request.method == 'POST':
        postSno = request.POST.get('postsno')
        post = Post.objects.get(sno=postSno)
        user = request.user
        comment = request.POST.get('newcomment')
        create_comment = BlogComment.objects.create(
            comment=comment, post=post, user=user)
        create_comment.save()
        path_red = request.POST.get('next', '/')
        return redirect(path_red)
