from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=75)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True, blank=True)
    postImage = models.ImageField(upload_to='static/tmp/')
    slug=models.SlugField(max_length=40)
    def __str__(self):
        return self.title + " by "+self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    time = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.sno)
