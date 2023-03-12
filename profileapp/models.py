from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='photos/',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'profileapp'

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        return self.image.url

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'profileapp'

    def __str__(self):
        return self.title

