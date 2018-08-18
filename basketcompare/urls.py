from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from products import views
from django.contrib.auth.views import login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
import products.views
from basketcompare.settings import base, development, production
from django.contrib.sitemaps.views import sitemap
import os, socket

from products.sitemaps import Product_Sitemap, Category_Sitemap, SubCategory_Sitemap, Fixed_Sitemap

basket_compare_sitemaps = {
    'products': Product_Sitemap,
    'categories': Category_Sitemap,
    'subcategories': SubCategory_Sitemap,
    'fixed_sitemap': Fixed_Sitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': basket_compare_sitemaps}),
    path('account/', products.views.account, name='account'),
    url(r'^login/$', products.views.login, name='login'),
    url(r'^register/', products.views.sign_up, name='register'),
    path('', products.views.home, name='home'),
    path('about/', products.views.about, name='about'),
    path('<slug>/p/<int:code>/', products.views.pdp, name='pdp'),
    url(r'^c/(?P<subcategory_slug>[-\w]+)/$', products.views.plp, name='plp'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', products.views.category_landing, name='category_landing'),
    url(r'^search', products.views.search_page, name='category_landing'),
    url(r'^favourites/', products.views.favourites, name='favourites'),
    url(r'^logout/$', products.views.logout, name='logout'),
    url(r'^password-reset$', PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    url(r'^password-reset/done$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetDoneView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    ]

urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)

if "DESKTOP" in socket.gethostname():
    urlpatterns += static(development.MEDIA_URL, document_root=development.MEDIA_ROOT)
else:
    urlpatterns += static(production.MEDIA_URL, document_root=production.MEDIA_ROOT)
