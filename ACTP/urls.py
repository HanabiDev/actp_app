from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin', include('backend.urls')),
    url(r'^', include('frontend.urls', 'frontend')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
