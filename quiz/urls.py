from django.contrib import admin
from django.urls    import path,include, re_path

from rest_framework import permissions
from drf_yasg       import openapi
from drf_yasg.views import get_schema_view

schema_url_patterns = [ 
    path('', include('users.urls')),
    ]

schema_view = get_schema_view(
    openapi.Info(
        title           = "Quiz_Tec API",
        default_version = "v1",
        description     = "Quiz_Tec API document",
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(email="auddwd19@naver.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('questions/', include('questions.urls')),




    #swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
] 

