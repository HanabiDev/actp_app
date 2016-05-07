from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^/$', 'backend.views.home', name='admin_home'),
    url(r'^/login/$', 'backend.views.login_user', name='backend_login'),
    url(r'^/logout/$', 'backend.views.logout_user', name='backend_logout'),
    url(r'^/clubes/', include('clubs.urls', 'clubs')),
    url(r'^/socios/', include('partners.urls', 'partners')),
]

