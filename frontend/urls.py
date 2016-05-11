from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'registro/$', 'frontend.views.affiliation', name='affiliation'),
    url(r'registro-completo/$', 'frontend.views.affiliation_success', name='affiliation_success'),

]