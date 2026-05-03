from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

from datetime import datetime


def health_check(request):
    return JsonResponse({
        'status': 'OK',
        'timestamp': datetime.now().isoformat(),
        'service': 'Django Backend'
    })


def api_test(request):
    return JsonResponse({
        'message': 'Hello from Django API!',
        'method': request.method,
        'path': request.path
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check),
    path('api/test/', api_test),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
