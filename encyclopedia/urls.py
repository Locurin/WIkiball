from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.entries, name="entries"),
    path("search", views.search, name="search"),
    path("random", views.random_entry, name="random"),
    path("new", views.new_entry, name="new"),
    path("edit", views.get_edit, name="edit"),
    path("edited", views.edit, name="edited"),
    path("articles", views.articles, name="articles")
]
