from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.

def main(request):
    return render(request, 'main.html')


class ArticleListView(ListView):
	model = Article
	queryset = Article.objects.all()
	template_name = "main.html"
	paginate_by = 8
