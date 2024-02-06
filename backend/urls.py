"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usermanagement.views import _logout, _login
from django.conf import settings
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from django.shortcuts import redirect
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


schema_view1 = get_schema_view(
    openapi.Info(
        title="User Management API",
        default_version='v1',
        #   description="Test description",
        #   terms_of_service="https://www.google.com/policies/terms/",
        #   contact=openapi.Contact(email="contact@snippets.local"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[],
)
schema_view = get_swagger_view(title='User Management Portal')


def docs(request):
    return redirect('/api/v1/docs')


urlpatterns = [
    path('', docs, name='redirect-docs'),
    path('api/admin/', admin.site.urls),
    # path('api/', include('usermanagement.urls')),
    path('accounts/login/', _login, name='session-login'),
    path('accounts/logout/', _logout, name='session-logout'),
    path(
            'api/v1/',
            include([
                path('docs/', schema_view, name='schema-swagger-ui'),
                path('redocs/',
                     schema_view1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                ##### JWT Authentication API Routes #####
                path('user/', include('usermanagement.urls')),

        ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = urlpatterns + [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
