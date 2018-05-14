from django.db import models
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    time = models.DateTimeField(default = datetime.now, blank = True)
    body = models.TextField()
    image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-time"]

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(default = datetime.now, blank = True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name