from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="publié")
    content = models.TextField(blank=True, verbose_name="contenue")
    image = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def publier(self):
        if self.author:
            return f"cette article a été publier par {self.author.username} le {self.created_on}"
        return "Cette aticle pas encore été publier"