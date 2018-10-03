from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Category(models.Model):
	category_name 					= models.CharField(primary_key=True, max_length=120, null=False, blank=True, unique=True)
	category_slug 					= models.SlugField(unique=True, null=True, blank=True)
	category_description			= models.TextField(null=True, blank=True)	

	def save(self, *args, **kwargs):
		self.category_slug = slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('category_landing', args=[self.category_slug])


class SubCategory(models.Model):
	subcategory_name 				= models.CharField(primary_key=True, max_length=120, null=False, blank=True, unique=True)
	subcategory_slug 				= models.SlugField(unique=True, null=True, blank=True)
	subcategory_description			= models.TextField(null=True, blank=True)
	category_name					= models.ForeignKey(Category, on_delete=models.CASCADE, to_field="category_name", null=True)

	def save(self, *args, **kwargs):
		self.subcategory_slug = slugify(self.subcategory_name)
		super(SubCategory, self).save(*args, **kwargs)

	def __str__(self):
		return self.subcategory_name

	def get_absolute_url(self):
		return reverse('plp', args=[self.subcategory_slug])

class Merchant(models.Model):

	merchant_choices = (
	('basket compare', 'Basket Compare'),
	('bq', 'B&Q'),
	('homebase', 'Homebase'),
	('screwfix', 'Screwfix'),
	('selco', 'Selco'),
	('toolstation', 'Toolstation'),
	('tradepoint', 'Tradepoint'),
	('travis perkins', 'Travis Perkins'),
	('wickes', 'Wickes')
	)

	merchant = models.CharField(primary_key=True, null=False, blank=True, choices=merchant_choices, max_length=50, unique=True)

	def __str__(self):
		return self.merchant


class Product(models.Model):
	# Basket Compare Info

	product_type_choices = (
		('master_product', 'master_product'),
		('compared_product', 'compared_product')
		)

	bc_sku 							= models.IntegerField(null=True, blank=True)
	product_type					= models.CharField(null=True, blank=True, choices=product_type_choices, max_length=50)
	merchant 						= models.ForeignKey(Merchant, on_delete=models.CASCADE, to_field="merchant", null=False)

	category						= models.ForeignKey(Category, on_delete=models.CASCADE, to_field="category_name", null=True)
	sub_category					= models.ForeignKey(SubCategory, on_delete=models.CASCADE, to_field="subcategory_name", null=True)
	

	product_sku_1 					= models.CharField(null=True, blank=True, max_length=250)
	product_sku_2 					= models.CharField(null=True, blank=True, max_length=250)
	product_brand					= models.CharField(null=True, blank=True, max_length=250)
	product_description 			= models.CharField(null=True, blank=True, max_length=250)
	product_pack_size 				= models.CharField(null=True, blank=True, max_length=250)
	product_url 					= models.CharField(null=True, blank=True, max_length=250)
	product_price 					= models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
	product_offer 					= models.CharField(null=True, blank=True, max_length=250)

	product_slug					= models.SlugField(null=True, blank=True, max_length=100)


	def save(self, *args, **kwargs):
			self.product_slug = slugify(self.product_description)
			super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.product_description

	def get_absolute_url(self):
		return reverse('pdp', args=[self.product_slug, self.bc_sku])

	# @property
	# def min_price(self):
	# 	prices = [self.wickes_price, self.wickes_2_price, self.bq_price, self.bq_2_price]
	# 	try:
	# 		min_price = min(x for x in prices if x is not None)
	# 	except ValueError:
	# 		min_price = ""
	# 	return min_price



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	favourites = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return self.user.username

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Project_Item(models.Model):
	item = models.ManyToManyField(Product, blank=True)
	quantity = models.PositiveIntegerField()

class Project(models.Model):
	name = models.CharField(null=False, blank=False, max_length=50)
	items = models.ManyToManyField(Project_Item, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username", null=False)
	merchants = models.ManyToManyField(Merchant, blank=False)

	class Meta:
		unique_together = ('name', 'user')
















