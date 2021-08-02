from django.contrib import admin
from .models import Article, Category, Image
from tinymce.widgets import TinyMCE
from django.db import models



class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		("Meta", {"fields": ["meta_title"]}),
		("Title/date", {"fields": ["article_slug", "article_header_image_url", "article_title", "article_description", "article_published"]}),
		("Content", {"fields": ["article_content"]}),
		("Category", {"fields": ["article_category"]}),
		("Public", {"fields": ["is_public"]}),
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}	
	}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Image)
