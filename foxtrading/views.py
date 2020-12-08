from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post


def foxLogin(request):
    return render(request, 'login.html')


def foxHome(request):
    if request.user.is_authenticated:
        newpost = Post.objects.all().order_by('-time')[0:3]
        context = {'newpost': newpost, 'sbar': 'blog'}
        return render(request, 'home.html', context)
    else:
        messages.warning(request, "invalid login")
        return redirect('/')


def foxSignup(request):
    return render(request, 'signup.html')


def foxLogout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('/')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    return render(request, 'login.html')


def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 15 or len(username) < 4:
            messages.error(
                request, "User Name must be between 3 to 15 characters")
            return redirect('/signup')
        if not username.isalnum():
            messages.error(request, 'User Name must be Numbers and Letters')
            return redirect('/signup')
        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect('/signup')

        myuser = User.objects.create(
            username=username, email=email, password=pass1, first_name=fname, last_name=lname)
        myuser.save()
        messages.success(request, "Please log in to continue!")
        return redirect('/')
    else:
        return HttpResponse("404 Not Found !")
