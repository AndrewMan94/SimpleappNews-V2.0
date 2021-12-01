from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    subscribers = models.ManyToManyField(User, through="CategorySubscribers")

    def __str__(self):
        return self.name


class Post(models.Model):
    article = "AR"
    news = "NW"
    POST_TYPE = [(article, 'Статья'), (news, 'Новость')]

    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=POST_TYPE, default=article)
    created = models.DateTimeField(auto_now_add=True)
    id_post_category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=255)
    text = models.TextField()



class PostCategory(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
