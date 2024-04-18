from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('doctors/', include('doctors.urls')),
    path('patient/', include('patient.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Fazemos essa configuração para exibir o caminho como link das imagens carregadas no projeto. 
