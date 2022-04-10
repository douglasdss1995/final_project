from celery import shared_task

from movie import actions, models


@shared_task(queue='default')
def send_announcement(announcement: 'models.Announcement'):
    actions.AnnouncementActions.send_announcement(announcement)
