import binascii
import os

from django.db import models
from django.dispatch import receiver
from django.utils import timezone


#
# @receiver(models.signals.pre_save, sender=ApiKey)
# def api_token_pre_save(sender, **kwargs):
#     instance = kwargs['instance']
#     instance.updated = timezone.now()
#     if instance.created is None:
#         instance.created = timezone.now()


# @receiver(models.signals.pre_save, sender=CommunityChargeSplits)
# def community_charge_splits_pre_save(sender, **kwargs):
#     instance = kwargs['instance']
#     if instance.rent_dynamics_split + instance.partner_split + instance.community_split != instance.amount:
#         # this should be a real exception not a generic one -- skyler
#         raise Exception('Splits must equal Amount')
