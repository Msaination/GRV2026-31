from django.db import router
from django.urls import path
from .views import CustomRouter, TownPropertyViewSet, TownDetailViewSet
# from .views import TownPropertyViewSet

router = CustomRouter()
router.register(r'', TownPropertyViewSet, basename='township')

# urlpatterns = router.urls
urlpatterns = [

    path('<int:pk>', TownDetailViewSet.as_view(), name='town_details'), 

] + router.urls

