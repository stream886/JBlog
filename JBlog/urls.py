"""JBlog URL Configuration

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
# from django.urls import path
from django.conf.urls import url

import xadmin

from main.views import index, contact, blog, blogs, blogs_archives, blogs_category, blogs_tag, blogs_search

urlpatterns = [
    url(r'^index/admin/', admin.site.urls),
    url(r'^index/xadmin/', xadmin.site.urls),

    url(r'^index/', index, name='index'),

    url(r'^blogs/', blogs, name='blogs'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', blogs_archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/', blogs_category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/', blogs_tag, name='tag'),

    url(r'^blog/(?P<pk>[0-9]+)/', blog, name='blog'),

    url(r'^contact/', contact, name='contact'),
]
