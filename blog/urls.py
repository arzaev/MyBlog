from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.ArticleListView.as_view(), name='main'),
]
