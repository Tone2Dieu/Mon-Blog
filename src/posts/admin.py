from django.contrib import admin
from . import models
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
   list_display = ('title', 'published', 'created_on', 'last_updated')
   list_editable = ('published',)


admin.site.register(models.BlogPost, BlogPostAdmin)
