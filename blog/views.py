from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category

# Create your views here.

def main(request):
    return render(request, 'main.html')


class ArticleListView(ListView):
	model = Article
	queryset = Article.objects.all()
	template_name = "main.html"
	paginate_by = 9

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class ArticleListCategoryView(ListView):
	template_name = "main.html"
	paginate_by = 9 

	def get_queryset(self):
		return Article.objects.filter(article_category=self.kwargs['category_id'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
