from importlib import import_module

from django.apps import apps
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from hotel import views
from reserva_hotel import settings


def include_api_urls(version, namespace):
    includes = []

    for app in apps.get_app_configs():
        try:
            urlconf_module = import_module(f'{app.name}.urls')
            if hasattr(urlconf_module, f'{version}_api_urlpatterns'):
                patterns = getattr(urlconf_module, f'{version}_api_urlpatterns')
            else:
                patterns = None
        except ModuleNotFoundError:
            pass
        else:
            if patterns:
                prefix = getattr(urlconf_module, 'app_api_prefix', app.name)
                if prefix:
                    prefix += '/'
                includes.append(
                    path(f'{prefix}api/{version}/', include((patterns, app.name), namespace=app.name))
                )

    return include((includes, namespace), namespace)


v1_api_urlpatterns = [
    path(settings.SITE_PATH, include_api_urls('', namespace=''))
]
urlpatterns = [
    path('cheapest/', views.CheapestHotel.as_view()),
    path('api/v1/docs/', include_docs_urls(
        'API v1.0.0', public=True, permission_classes=[])
         ),

]
