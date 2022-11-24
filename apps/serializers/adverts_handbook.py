from rest_framework.serializers import ModelSerializer

from apps.models import Category, Complain, Region, District


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'parent')


class ComplainModelSerializer(ModelSerializer):
    class Meta:
        model = Complain
        fields = ('advert', 'text', 'type')


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('name', 'region')
