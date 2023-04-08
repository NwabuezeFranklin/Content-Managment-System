from django.shortcuts import render, redirect
from .forms import ProfileForm, ImageForm
from .models import Profile, Image, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
           messages.error(request, 'User not found')
           
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User not found')
    context = {'page': page}
    return render(request, 'App/login.html', context)


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'User logged out successfully')
        return redirect('home')
    context = {}
    return render(request, 'App/logoutUser.html', context)

            
def registerUser(request):
    page = 'Register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a new profile object and associate it with the new user
            profile = Profile.objects.create(user=user)
            profile.user_id = user.id
            profile.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'An error occurred during registration')
        
    context = {'form': form}
    return render(request, 'App/login.html', context)


def home(request):
     profiles = Profile.objects.all()
     context = {'profiles': profiles}
     return render(request, 'home.html', context)
 

def profile(request):
    user = request.user
    # Check if the user already has a profile
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None

    if profile:
        # If the user already has a profile, redirect to their profile page
        return redirect('update', profile.id)
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if user.user == request.user:
                return redirect('profileList')
                
            user.user = request.user
            user.save()
            return redirect('home')
    context = {'form': form}   
    return render(request, 'App/profile.html', context)


def myProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    user = User.objects.get(id=pk)
    profiles = Profile.objects.all()
    users = User.objects.all()
    posts = Image.objects.all()
    post = Image.objects.filter(user=user).annotate(num_articles=Count('user'))
    
    #image = Image.objects.all()
    #comments = Comment.objects.all()
    context = {'profiles': profiles, 'user': user, 'profile': profile, 'post': post,}
    return render(request, 'App/myProfile.html', context)
    
#@login_required(login_url='loginUser')
def profileList(request,pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    profiles = Profile.objects.all()
    user = User.objects.all()
    post = Image.objects.all()
    users = User.objects.get(id=pk)
    posts = users.image_set.all()
    contents = Image.objects.filter(
        Q(user__username__icontains=q) |
        Q(topic__icontains=q)
            
    )
    context = {'profiles': profiles, 'user': user, 'post': post, 'users': users, 'posts': posts, 'contents': contents}
    return render(request, 'App/profileList.html', context)

def guestProfile(request):
    #if request.user.is_authenticated():
        # If the user already has a profile, redirect to their profile page
        #return redirect('profileList', user.id)
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    profiles = Profile.objects.all()
    user = User.objects.all()
    post = Image.objects.all()
    contents = Image.objects.filter(
        Q(user__username__icontains=q) |
        Q(topic__icontains=q)
            
    )
    context = {'profiles': profiles, 'user': user, 'post': post, 'contents': contents}
    return render(request, 'App/guestProfile.html', context)


def update(request, pk):
    form = Profile.objects.get(id=pk)
    form_update = ProfileForm(instance=form)
    if request.method == 'POST':
        form_update = ProfileForm(request.POST, request.FILES, instance=form,)
        if form_update.is_valid():
            form_update.save()
            return redirect('myProfile', pk=form.id)
    context = {'form_update': form_update}   
    return render(request, 'App/update.html', context)


def uploads(request, pk):
    form = ImageForm()
    #num = Profile.objects.get(id)
    users = User.objects.get(id=pk)
    profile = Profile.objects.get(id=pk)
    user = User.objects.get(id=pk)
    post = user.image_set.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES,)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('profileList', pk=users.id)
    context = {'form': form, 'post':post, 'profile': profile, 'users': users}
    return render(request, 'App/uploads.html', context)
        
        
def comments(request, pkm, pk, pkr):
    user = User.objects.get(id=pkm)
    profile = Profile.objects.get(id=pkm)
    post = Image.objects.get(id=pkr)
    replies = post.comment_set.all()
    count = replies.count()
    if request.method == 'POST':
        comments = Comment.objects.create(
            user = request.user,
            image = post,
            text = request.POST.get('text'),
        )   
        return redirect('comments', pkm = user.id, pk = post.user.id, pkr = post.id,)
        
    context = {'post': post, 'user': user, 'replies': replies, 'count': count, 'profile': profile,}
    return render(request, 'App/comments.html', context, )


def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profileList')
    return render(request, 'App/delete.html', {'obj': profile})