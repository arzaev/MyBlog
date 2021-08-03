from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.ArticleListView.as_view(), name='main'),
	path('<int:pk>/', views.ArticleDetailView.as_view()),
	path('category/<int:category_id>', views.ArticleListCategoryView.as_view()),
]
