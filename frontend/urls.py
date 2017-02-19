from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'inscripcion/$', 'frontend.views.subscribe', name='subscribe'),
    url(r'registro-evento/$', 'frontend.views.renovation', name='renovate'),
    url(r'registro/$', 'frontend.views.affiliation', name='affiliation'),
    url(r'registro-completo/$', 'frontend.views.affiliation_success', name='affiliation_success'),

]