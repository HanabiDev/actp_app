from django.conf.urls import include, url
import clubs

urlpatterns = [
    # Examples:
    url(r'^$', 'partners.views.home', name='home'),
    url(r'^reporte/$', 'partners.views.report', name='report'),
    url(r'^nuevo/', 'partners.views.create_partner', name='new'),
    url(r'^ver/(?P<partner_id>\d+)/$', 'partners.views.read_partner', name='view'),
    url(r'^qr/$', 'partners.views.get_qr', name='qr'),
    url(r'^editar/(?P<partner_id>\d+)/$', 'partners.views.update_partner', name='edit'),
    url(r'^editar/(?P<partner_id>\d+)/cambiar-clave/$', 'partners.views.update_password', name='pass'),
    url(r'^aceptar/(?P<partner_id>\d+)/$', 'partners.views.accept_member', name='accept'),
    url(r'^cambiar-estado/(?P<partner_id>\d+)/$', 'partners.views.toggle_status', name='toggle_active'),
]
