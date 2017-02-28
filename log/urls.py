from django.conf import settings
from django.conf.urls import include, url

from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/add/$', views.add_steps, name='add_steps'),
    url(r'^home/top/$', views.top, name='top')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
