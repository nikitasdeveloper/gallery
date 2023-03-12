from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Photo, Video
from .forms import PhotoForm, VideoForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('gallery')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            return redirect('gallery')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

@login_required
def gallery(request):
    photos = Photo.objects.all()
    videos = Video.objects.all()
    return render(request, 'gallery.html', {'photos': photos, 'videos': videos})

@login_required
def view_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'view_photo.html', {'photo': photo})

@login_required
def view_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'view_video.html', {'video': video})

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user == photo.uploader:
        photo.delete()
    return redirect('gallery')


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.user == video.uploader:
        video.delete()
    return redirect('gallery')



@login_required
def profile(request):
    user = request.user
    photos = user.photo_set.all()
    videos = user.video_set.all()
    return render(request, 'myprofile.html', {'user': user, 'photos': photos, 'videos': videos})
