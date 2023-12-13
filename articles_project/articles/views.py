from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from .models import Article, Author, Magazine, KeyWords
from django.urls import reverse_lazy
from django.db.models import Q


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
    context_object_name = 'articles_queryset'
    model = Article

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(Q(title__icontains=query)
                                          | Q(keywords__word__icontains=query)
                                          | Q(author__name__icontains=query)
                                          | Q(author__surname__icontains=query))
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class ArticleDetailView(DetailView):
    template_name = 'article-detail.html'
    context_object_name = 'article'
    model = Article