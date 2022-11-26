from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Complain, Region, District
from apps.serializers import CategoryModelSerializer, ComplainModelSerializer, RegionModelSerializer, \
    DistrictModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class DistrictModelViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictModelSerializer


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer


class ComplainModelViewSet(ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainModelSerializer
