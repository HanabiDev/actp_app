from django.conf.urls import include, url
import clubs

urlpatterns = [
    # Examples:
    url(r'^$', 'partners.views.home', name='home'),
    url(r'^nuevo/', 'partners.views.create_partner', name='new'),
    url(r'^ver/(?P<club_id>\d+)/$', 'clubs.views.read_club', name='view'),
    url(r'^qr/$', 'partners.views.get_qr', name='qr'),
    url(r'^editar/(?P<partner_id>\d+)/$', 'partners.views.update_partner', name='edit'),
    url(r'^editar/(?P<partner_id>\d+)/cambiar-clave/$', 'partners.views.update_password', name='pass'),
    url(r'^cambiar-estado/(?P<partner_id>\d+)/$', 'clubs.views.toggle_status', name='toggle_active'),
]
