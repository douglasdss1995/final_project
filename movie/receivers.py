from django.db.models.signals import post_save
from django.dispatch import receiver
from kombu.exceptions import OperationalError

from movie import models, tasks


@receiver(post_save, sender=models.Announcement, dispatch_uid='send_announcement', weak=False)
def send_announcement(instance, **kwargs):
    try:
        tasks.send_announcement(instance)
    except OperationalError as error:
        raise Exception(f'Broker connection error {error}')
