"""game0verflows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from game0verflowsapp import views
from django.contrib import admin
admin.autodiscover()

handler404 = views.error
handler500 = views.error
handler403 = views.error
handler400 = views.error


urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    url(r'^failles-applicatives/$', views.failles_applicatives),
    url(r'^failles-applicatives/(?P<id>[0-9]+)/(?P<name>[\w-]+)/$', views.post),

    url(r'^failles-web/$', views.failles_web),
    url(r'^failles-web/(?P<id>[0-9]+)/(?P<name>[\w-]+)/$', views.post),

    url(r'^scripts/$', views.scripts),
    url(r'^scripts/(?P<id>[0-9]+)/(?P<name>[\w-]+)/$', views.post),

    url(r'^actualites/$', views.actualites),
    url(r'^actualites/(?P<id>[0-9]+)/(?P<name>[\w-]+)/$', views.post),
]
