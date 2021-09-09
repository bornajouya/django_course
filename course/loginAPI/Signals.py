# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
import time

@receiver(post_save, sender=User)
def change_lastname(sender, instance, created, **kwargs):
    time.sleep(5)
    # sender.user_name = sender.user_lastname
    # sender.save()

