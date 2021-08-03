from datetime import datetime
from django.db import models
from django.urls import reverse
from tinymce import models as tm

# Create your models here.


class Category(models.Model):
	category_name = models.CharField(max_length=255, unique=True)
	category_slug = models.SlugField(max_length=255)

	def __str__(self):
		return self.category_slug


class Article(models.Model):
	meta_title = models.CharField(max_length=255)
	article_header_image_url = models.CharField(max_length=255)
	article_description = models.TextField()
	article_title = models.CharField(max_length=255)
	article_content = tm.HTMLField()
	article_published = models.DateTimeField("date publiched", default=datetime.now())
	article_slug = models.SlugField(max_length=255, unique=True)
	article_category = models.ManyToManyField(Category)
	is_public = models.BooleanField(default=False)

	def __str__(self):
		return self.article_title

	def get_absolute_url(self):
		return reverse('article', args=[str(self.article_slug)])


class Image(models.Model):
	image = models.ImageField(upload_to='')

	def __str__(self):
		return str(self.id)
