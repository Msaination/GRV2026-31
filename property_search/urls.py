from django.db import router

from rest_framework.routers import DefaultRouter
from .views import CustomRouter, FarmPropertyViewSet
# from .views import FarmPropertyViewSet

router = CustomRouter()
# router.register(r'town', TownPropertyViewSet)
router.register(r'farm', FarmPropertyViewSet)

urlpatterns = router.urls