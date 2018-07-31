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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', views.account, name='account'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/', views.sign_up, name='register'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug>/p/<int:code>/', views.pdp, name='pdp'),
    url(r'^c/(?P<subcategory_slug>[-\w]+)/$', views.plp, name='plp'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_landing, name='category_landing'),
    url(r'^search', views.search_page, name='category_landing'),
    url(r'^favourites/', views.favourites, name='favourites'),
    url(r'^logout/$', views.logout, name='logout'),
    # url (regex, view, template to render)
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
