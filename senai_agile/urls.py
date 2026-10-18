from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Inclui todas as rotas do app principal
]
# Servindo arquivos de mídia (imagens, uploads)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.http import FileResponse
from django.contrib.staticfiles import finders

def service_worker(request):
    response = FileResponse(open(finders.find('service-worker.js'), 'rb'), content_type='application/javascript')
    response['Service-Worker-Allowed'] = '/'
    response['Cache-Control'] = 'no-cache'
    return response

urlpatterns += [path('service-worker.js', service_worker, name='service_worker')]
