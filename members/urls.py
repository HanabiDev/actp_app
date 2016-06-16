from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'members.views.home', name='members_home'),
    url(r'^equipos/', 'members.views.read_equipments', 'equipments'),
    url(r'^equipos/nuevo/', 'members.views.create_equipment', 'new_equipment'),
]

