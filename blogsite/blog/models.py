from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=155)
    image = models.ImageField(upload_to='post/%Y-year/%m-month')
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} {self.email}'
