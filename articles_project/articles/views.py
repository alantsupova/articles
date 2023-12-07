from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from .models import Article, Author, Magazine, KeyWords
from django.urls import reverse_lazy


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'magazine', 'pages', 'keywords', 'author']
    template_name = 'article-create.html'
    success_url = reverse_lazy('list')


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'surname']
    template_name = 'author-create.html'
    success_url = reverse_lazy('list')


class MagazineCreateView(CreateView):
    model = Magazine
    fields = ['title', 'website', 'year', 'tom', 'number']
    template_name = 'magazine-create.html'
    success_url = reverse_lazy('list')


class KeyWordsCreateView(CreateView):
    model = KeyWords
    fields = ['word',]
    template_name = 'keywords-create.html'
    success_url = reverse_lazy('list')


class ArticleListView(ListView):
    template_name = 'article-list.html'
    model = Article
    context_object_name = 'articles'