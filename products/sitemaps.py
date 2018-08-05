from django.contrib.sitemaps import Sitemap
from products.models import Product, Category, SubCategory
from django.urls import reverse

class Product_Sitemap(Sitemap):
	def items(self):
		return Product.objects.all()

class Category_Sitemap(Sitemap):
	def items(self):
		return Category.objects.all()

class SubCategory_Sitemap(Sitemap):
	def items(self):
		return SubCategory.objects.all()

class Fixed_Sitemap(Sitemap):
	def items(self):
		return ['about', 'login', 'account', 'register']

	def location(self, item):
		return reverse(item)
