from rest_framework.viewsets import ModelViewSet

from apps.models import Advert
from apps.serializers import AdvertModelSerializer


class AdvertModelViewSet(ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer
