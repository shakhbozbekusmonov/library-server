from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",  # Replace with your project's API title
        default_version="v1",  # Replace with your project's API version
        description="Your project's API description",  # Replace with your project's API description
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Adjust permissions as needed
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path("swagger", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-swagger-ui"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
