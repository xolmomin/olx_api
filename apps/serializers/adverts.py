from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.models import Advert


class AdvertModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Advert
        exclude = ('views', 'phone_views_count', 'created_at')


class PhoneAdvertModelSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = ('phone',)
