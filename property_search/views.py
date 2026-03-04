from rest_framework import viewsets, filters
from rest_framework.routers import DefaultRouter, APIRootView
from rest_framework.response import Response
from .models import FarmProperty
from .serializers import FarmPropertySerializer
from rest_framework.pagination import LimitOffsetPagination



# CustomAPIRootView is a subclass of APIRootView that overrides the get method
# to include the count of farm properties in the API root response. 
# This allows clients to see how many farm properties are available when they access the API root endpoint.
class CustomAPIRootView(APIRootView):
    def get(self, request, *args, **kwargs):
        # Call the default root view
        response = super().get(request, *args, **kwargs)
        # Add farm property count
        farm_count = FarmProperty.objects.count()
        response.data['farm_property_count'] = farm_count
        return Response(response.data)

class CustomRouter(DefaultRouter):
    APIRootView = CustomAPIRootView

#Pagination class to limit the number of results returned in a single API response. 
# This helps improve performance and manageability when dealing with large datasets.
class FarmPropertyPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

class FarmPropertyViewSet(viewsets.ModelViewSet):
    queryset = FarmProperty.objects.all()
    serializer_class = FarmPropertySerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['location', 'size', 'price']

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sg_code_21', 'farm_name', 'physical_address']
    ordering_fields = ['sg_code_21', 'farm_name', 'physical_address', 'market_value']
    ordering = ['market_value']  # default ordering by market_value
    pagination_class = FarmPropertyPagination