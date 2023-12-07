from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-article/', ArticleCreateView.as_view(), name='create-article'),
    path('create-author/', AuthorCreateView.as_view(), name='create-author'),
    path('create-magazine/', MagazineCreateView.as_view(), name='create-magazine'),
    path('create-keywords/', KeyWordsCreateView.as_view(), name='create-keywords'),
    path('list/', ArticleListView.as_view(), name='list'),
    # path('detail/<int:pk>/', PizzaDetailView.as_view(), name='detail'),
    # path('buy/<int:pk>/', PizzaBuyView.as_view(), name='buy'),
]
