from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, CASCADE, ForeignKey


class User(AbstractUser):
    phone = CharField(max_length=25, null=True, blank=True)
    region = ForeignKey('apps.Region', CASCADE, null=True, blank=True)
    district = ForeignKey('apps.District', CASCADE, null=True, blank=True)
