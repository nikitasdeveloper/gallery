from django import forms
from .models import Photo, Video

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title','image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','video']
