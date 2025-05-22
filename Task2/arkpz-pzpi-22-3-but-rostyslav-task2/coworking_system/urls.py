from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Налаштування Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Coworking Management API",
        default_version='v1',
        description="API для управління корпоративними ресурсами у коворкінгах",
    ),
    public=True,
    permission_classes=[AllowAny],  # Дозволяємо доступ без авторизації
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
