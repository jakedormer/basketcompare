from django.contrib import admin
from import_export import resources
from .models import Product, Category, SubCategory, Profile, Merchant
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin

class productAdmin(admin.ModelAdmin):
	class Meta:
		model = Product

admin.site.register(Product, productAdmin)

class merchantAdmin(admin.ModelAdmin):
	class Meta:
		model = Merchant

admin.site.register(Merchant, merchantAdmin)

class categoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Category, categoryAdmin)

class subcategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = SubCategory

admin.site.register(SubCategory, subcategoryAdmin)

class ProductResource(resources.ModelResource):
	class Meta:
		model = Product

class ProductAdmin(ImportExportModelAdmin):
	resource_class = ProductResource
	list_display = ("bc_sku", "product_description", "product_type", "product_price")
	list_filter = ["product_type"]

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile, profileAdmin)

