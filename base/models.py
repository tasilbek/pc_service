from django.db import models

# Create your models here.

class Contact(models.Model):
    pass

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()
    image = models.FileField(upload_to='post-image')

    def __str__(self):
        return self.title