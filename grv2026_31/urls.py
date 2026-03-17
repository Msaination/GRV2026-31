from django.contrib import admin
from django.urls import path, include
from .api_root import APIRootView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', APIRootView.as_view(), name='api-root'),
    path('api/farms', include('property_search.urls')),
    path('api/townships', include('township_properties.urls'))
]
