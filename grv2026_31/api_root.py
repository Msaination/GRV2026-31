from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from property_search.models import FarmProperty
from township_properties.models import TownshipProperty


class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            # "farm": request.build_absolute_uri(reverse("farm")),
            "farm_property_count": FarmProperty.objects.count(),
            # "township": request.build_absolute_uri(reverse("township")),
            "township_property_count": TownshipProperty.objects.count(),
        })
