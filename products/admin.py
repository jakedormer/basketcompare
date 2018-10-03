from django.contrib import admin
from import_export import resources
from .models import Product, Category, SubCategory, Profile, Merchant
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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


class CategoryResource(resources.ModelResource):
	class Meta:
		model = Category

class CategoryAdmin(ImportExportModelAdmin):
	resource_class = CategoryResource

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile, profileAdmin)

class MyUserAdmin(UserAdmin):
    ordering = ('date_joined', )

    list_display = ('username', 'email', 'date_joined', 'last_login', 'first_name', 'last_name', 'is_staff')

# finally replace the default UserAdmin with yours
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)