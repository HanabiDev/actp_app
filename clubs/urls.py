from django.conf.urls import include, url
import clubs

urlpatterns = [
    # Examples:
    url(r'^$', 'clubs.views.home', name='home'),
    url(r'^nuevo/', 'clubs.views.create_club', name='new'),
    url(r'^editar/(?P<club_id>\d+)/$', 'clubs.views.update_club', name='edit'),
    url(r'^cambiar-estado/(?P<club_id>\d+)/$', 'clubs.views.toggle_status', name='toggle_active'),
]
