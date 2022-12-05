from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from article.manager import ArticleManager


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)


class Article(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='author')
    headline = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=options, default='draft')
    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()  # default manager
    article_manager = ArticleManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.slug])
