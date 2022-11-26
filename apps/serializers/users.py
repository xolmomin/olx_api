from rest_framework.serializers import ModelSerializer

from apps.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ()
