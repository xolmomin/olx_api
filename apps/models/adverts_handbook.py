from django.db.models import CharField, SlugField, CASCADE, ImageField, SET_NULL, Model, ForeignKey, \
    TextChoices
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Wishlist(Model):
    user = ForeignKey('apps.User', CASCADE)
    advert = ForeignKey('apps.Advert', CASCADE)

    class Meta:
        verbose_name = "Saralangan e'lon"
        verbose_name_plural = "Saralangan e'lonlar"


class AdvertImage(Model):
    image = ImageField(upload_to='adverts/images/')
    advert = ForeignKey('apps.Advert', CASCADE)


class CurrencyType(Model):
    currency = CharField(max_length=5)


class Complain(Model):
    class Type(TextChoices):
        SPAM = 'spam', 'Spam'
        INCORRECT = 'incorrect', "Noto'g'ri kategoriya"
        BANNED = 'banned', "Taqiqlangan mahsulot xizmati yoki tarkibi"
        OLD = 'old', 'eskirgan'
        WRONG_TYPE = 'wrong', 'Firibgarlik'

    advert = ForeignKey('apps.Advert', CASCADE)
    type = CharField(max_length=25, choices=Type.choices)
    text = CharField(max_length=512)


class Category(MPTTModel):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    image = ImageField(upload_to='category/images/', default='category/default.png')
    parent = TreeForeignKey('self', SET_NULL, null=True, blank=True)


class Region(Model):
    name = CharField(max_length=255)


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE)
