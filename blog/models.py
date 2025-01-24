from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog', default='blog/default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = HTMLField()
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return ('{}- {}'.format(self.id, self.title))
    
    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"pk": self.pk})
    