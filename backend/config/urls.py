"""config URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
]
