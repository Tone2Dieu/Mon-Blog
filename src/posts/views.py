from django.shortcuts import render
from django.views import generic
from datetime import datetime
from . import models, form
from django.urls import reverse_lazy

# Create your views here.

homeImage = "home-image"

def home(request):
    return render(request, "blog/index.html", {"date": datetime.today(), "homeImage": homeImage})


class ListeArticle(generic.ListView):
    model = models.BlogPost
    template_name = "blog/list-articles.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return  queryset
        return queryset.filter(published=True)


class NewArticle(generic.CreateView):
     model = models.BlogPost
     template_name = "blog/new-article.html"
     form_class = form.BlogPostForm

     success_url = reverse_lazy("articles")

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['submit'] = "Enregistrer"
         return  context


class MyArticle(generic.DetailView):
    model = models.BlogPost
    template_name = "blog/my-article.html"
    context_object_name = "post"


class UpdateArticle(generic.UpdateView):
    model = models.BlogPost
    template_name = "blog/new-article.html"
    form_class = form.BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit'] = "Modifier"
        return context


class DeleteArticle(generic.DeleteView):
    model = models.BlogPost
    template_name = "blog/delete-article.html"
    context_object_name = "post"

    success_url = reverse_lazy("articles")