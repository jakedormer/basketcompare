"""basketcompare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from products import views
from django.contrib.auth.views import login
import products.views
from basketcompare.settings import base

urlpatterns = [
    path('admin/', admin.site.urls),
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
]


urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
