from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Coworking Management API",
        default_version='v1',
        description="API для управління корпоративними ресурсами у коворкінгах",
    ),
    public=True,
    permission_classes=[AllowAny],  # Дозволяємо доступ без авторизації
    # Видалено security_definitions і security — тепер налаштовуємо в settings.py
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # логін, отримання токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # оновлення токена
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

