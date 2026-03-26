from django.db import router
from django.urls import path
from .views import CustomRouter, FarmPropertyViewSet, FarmDetailViewSet
# from .views import FarmPropertyViewSet


router = CustomRouter()
# router.register(r'town', TownPropertyViewSet)
router.register(r'', FarmPropertyViewSet, basename='farm')

# urlpatterns = router.urls

urlpatterns = [

    path('<int:pk>', FarmDetailViewSet.as_view(), name='farm_details'),
    # path('<int:pk>/export', FarmDetailViewSet.as_view(), name='farm_details'),

] + router.urls