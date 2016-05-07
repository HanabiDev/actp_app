from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'registro/$', 'frontend.views.affiliation', name='affiliation'),

]