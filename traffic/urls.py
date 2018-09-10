from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('getValue/', views.index, name='index'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)