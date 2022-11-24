from django.db.models import CharField, CASCADE, PROTECT, Model, ForeignKey, \
    IntegerField, TextChoices, BooleanField, DateTimeField


class Advert(Model):
    class Type(TextChoices):
        ACTIVE = 'active', 'Faol'
        WAITING = 'waiting', 'Kutayotgan'
        UNPAID = 'unpaid', "To'lanmagan"
        FINISHED = 'finished', 'Nofaol'
        MODERATED = 'moderated', 'Rad etilgan'

    # class PaymentType(TextChoices):
    #     FREE = 'free', 'bepul'
    #     EXCHANGE = 'exchange', 'ayirboshlash'
    #     CASH = 'cash', 'narx'

    # class StatusType(TextChoices):
    #     NEW = 'new', 'yangi'
    #     USED = 'used', 'ishlatilgan'

    class OwnerType(TextChoices):
        private = 'private', 'Xususiy'
        business = 'business', 'Biznes'

    title = CharField(max_length=255)
    description = CharField(max_length=255)
    # payment_type = CharField(max_length=10, choices=PaymentType.choices)
    currency_type = ForeignKey('apps.CurrencyType', PROTECT)
    price = IntegerField(null=True, blank=True)
    is_negotiable = BooleanField(null=True, blank=True)
    owner_type = CharField(max_length=10, choices=OwnerType.choices)
    # status = CharField(max_length=5, choices=StatusType.choices)
    region = ForeignKey('apps.Region', CASCADE)
    district = ForeignKey('apps.District', CASCADE)
    phone = CharField(max_length=25, null=True, blank=True)

    type = CharField(max_length=15, choices=Type.choices, default=Type.WAITING)

    views = IntegerField(default=0)
    phone_views_count = IntegerField(default=0)

    author = ForeignKey('apps.User', CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"

    @property
    def wishlist_count(self):
        return self.wishlist_set.count()
