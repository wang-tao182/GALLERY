from django.conf.urls import url

from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.home2),
] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)