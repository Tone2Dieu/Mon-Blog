from django import forms
from . import models


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = [
            "title",
            "created_on",
            "published",
            "content"
        ]