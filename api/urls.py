from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from rest_framework.documentation import include_docs_urls

from api.restful.viewsets import UsersViewSet, UserLoginViewSet

router = routers.DefaultRouter()
router.register(r"users", UsersViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="BMA APIs",
        default_version='v1',
        description="List of BMA APIs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alluaravind1313@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("register/", UsersViewSet.as_view({"post": "create"}), name="register"),
    path("login/", UserLoginViewSet.as_view({"post": "create"}), name="login"),
]
