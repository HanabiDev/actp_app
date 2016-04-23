from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'ACTP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^clubes/', include('clubs.urls', 'clubs')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
