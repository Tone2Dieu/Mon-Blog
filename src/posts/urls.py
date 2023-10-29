
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('articles', views.ListeArticle.as_view(), name="articles"),
    path('new-article/', views.NewArticle.as_view(), name='new-article'),
    path('article/<str:slug>', views.MyArticle.as_view(), name="article"),
    path('update-article/<str:slug>', views.UpdateArticle.as_view(), name="update-article"),
    path('delete-article/<str:slug>', views.DeleteArticle.as_view(), name="delete-article")

]