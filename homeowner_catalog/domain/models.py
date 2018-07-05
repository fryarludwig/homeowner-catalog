import datetime
import decimal

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

# from django.core.exceptions import ObjectDoesNotExist, ValidationError as DjangoValidationError
# from django.db.models.fields import BinaryField, DateTimeField as DjangoDateTimeField, DecimalField
# from django.db.models.fields.related import ForeignKey as DjangoForeignKey, OneToOneField
# from django.conf import settings


class OAuthToken(models.Model):
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=len('Bearer'), default='Bearer', editable=False)
    expires_in = models.DateTimeField(default=timezone.now)
    scope = models.CharField(max_length=255, default='read')

    @property
    def is_expired(self):
        return datetime.datetime.today() > self.expires_in

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if isinstance(self.expires_in, str):
            self.expires_in = int(self.expires_in)

        if isinstance(self.expires_in, int):
            self.expires_in = datetime.datetime.today() + datetime.timedelta(seconds=self.expires_in)

        super(OAuthToken, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                     update_fields=update_fields)

    def to_dict(self):
        token = {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'token_type': self.token_type,
            'expires_in': int((self.expires_in - timezone.now()).total_seconds()),
            'scope': self.scope
        }
        return token

    class Meta:
        db_table = 'oauth_token'


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Account', related_name='home_owner', on_delete=models.CASCADE)
    agents = ArrayField(models.IntegerField(blank=True, null=True), default=[])
    assistants = ArrayField(models.IntegerField(blank=True, null=True), default=[])

    class Meta:
        db_table = 'home'


class Location(models.Model):
    HOUSE = 0
    SHED = 1
    GARAGE = 2
    OUTSIDE = 3
    OTHER = 4
    UNKNOWN = 5

    Category = ((HOUSE, 'House'),
                (SHED, 'Shed'),
                (GARAGE, 'Garage'),
                (OUTSIDE, 'Outside'),
                (OTHER, 'Other'),
                (UNKNOWN, 'Unknown'))

    id = models.AutoField(primary_key=True)
    name = models.TextField()
    category = models.IntegerField(choices=Category, default=UNKNOWN)
    photos = models.ManyToManyField('Photo', related_name='photo_location', symmetrical=True)
    items = models.ManyToManyField('Item', related_name='item_location', symmetrical=True)

    class Meta:
        db_table = 'location'


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    home = models.ForeignKey(Home, related_name='home_photos', on_delete=models.CASCADE)
    location = models.ManyToManyField('Location', symmetrical=True)
    items = models.ManyToManyField('Item', symmetrical=True)

    class Meta:
        db_table = 'photo'


class Item(models.Model):
    EXCELLENT = 0
    GOOD = 1
    GOOD_ENOUGH = 2
    FAIR = 3
    POOR = 4
    AWFUL = 5
    UNKNOWN = 6

    Condition = ((EXCELLENT, 'Excellent'),
                 (GOOD, 'Good'),
                 (GOOD_ENOUGH, 'Good enough'),
                 (FAIR, 'Fair'),
                 (POOR, 'Poor'),
                 (AWFUL, 'Awful'),
                 (UNKNOWN, 'Unknown'))

    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey('Location', related_name='item_location', on_delete=models.PROTECT)
    previous_condition = models.IntegerField(choices=Condition, default=UNKNOWN, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'item'


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    location = models.ManyToManyField('Location', related_name='location_note', symmetrical=True)
    items = models.ManyToManyField('Item', related_name='item_note', symmetrical=True)

    class Meta:
        db_table = 'note'

# class


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    items = models.ManyToManyField('Item', blank=True)
    user = models.ForeignKey('Account', related_name='user_documents', on_delete=models.CASCADE)
    home = models.ForeignKey('Home', related_name='home_documents', on_delete=models.CASCADE)

    class Meta:
        db_table = 'document'


class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=140)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'account'
#
# # HSUAccount - holds information for user's Hydroshare account
# class UserAccount(models.Model):
#     user = models.OneToOneField(settings, null=True, blank=True, related_name='user_account', on_delete=models.CASCADE)
#     is_enabled = models.BooleanField(default=False)
#     ext_id = models.IntegerField(unique=True)  # external hydroshare account id
#     token = models.ForeignKey(OAuthToken, db_column='token_id', null=True, on_delete=models.CASCADE)
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         return super(UserAccount, self).save(force_insert=force_insert, force_update=force_update, using=using,
#                                                    update_fields=update_fields)
#
#     def delete(self, using=None, **kwargs):
#         return super(UserAccount, self).delete(using=using, keep_parents=True)
#     #
#     # @property
#     # def username(self):
#     #     return self.user.username
#     #     # return ODM2User.objects.filter(hydroshare_account=self.pk).first().user.username
#
#     def resources(self):
#         return ", ".join([str(r.id) for r in UserAccount.objects.filter(hs_account=self)])
#     resources.short_description = 'Resource IDs'
#
#     def get_token(self):
#         try:
#             return self.token.to_dict()
#         except ObjectDoesNotExist:
#             return None
#
#     def update_token(self, token_dict):  # type: (dict) -> None
#         if isinstance(self.token, OAuthToken):
#             self.token.access_token = token_dict.get('access_token')
#             self.token.refresh_token = token_dict.get('refresh_token')
#             self.token.token_type = token_dict.get('token_type')
#             self.token.expires_in = token_dict.get('expires_in')
#             self.token.scope = token_dict.get('scope')
#             self.token.save()
#         self.save()
#
#     def to_dict(self, include_token=True):
#         account = {
#             'id': self.pk,
#             'ext_id': self.ext_id,
#             'is_enabled': self.is_enabled
#         }
#         if include_token:
#             token = self.get_token()
#             if token:
#                 account['token'] = token
#         return account
#
#     class Meta:
#         db_table = 'user_account'
