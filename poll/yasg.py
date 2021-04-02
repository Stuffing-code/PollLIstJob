from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Poll API",
      default_version='v1',
      description="Test description",
      license=openapi.License(name="Poll License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]