from django.db import models

# Create your models here.
class Article(models.Model):
    url = models.URLField()    
    title = models.CharField(max_length=50)
    title_zh = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content_md = models.TextField()
    content_html = models.TextField()
    tags = models.CharField(max_length=30)
    views = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()