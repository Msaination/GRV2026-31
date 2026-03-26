from rest_framework.routers import DefaultRouter
from .views import TownshipObjectionViewSet, FarmObjectionViewSet

router = DefaultRouter()
router.register(r'township-objections', TownshipObjectionViewSet)
router.register(r'farm-objections', FarmObjectionViewSet)

urlpatterns = [
    # ... other paths ...
] + router.urls
