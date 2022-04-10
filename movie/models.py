from django.db import models
from django.utils.translation import gettext_lazy as _

from movie import managers


class ModelBase(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )
    active = models.BooleanField(
        null=False,
        default=True
    )

    class Meta:
        abstract = True


class Movie(ModelBase):
    title = models.CharField(
        db_column='title',
        max_length=256,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_('Title')
    )
    category = models.ForeignKey(
        to='Category',
        db_column='id_category',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='movies'
    )

    objects = managers.MovieManager()

    class Meta:
        managed = True
        db_table = '"movie"."movie"'
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')

    def __str__(self):
        return f'{self.title}'


class Subscriber(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=125,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_('Name')
    )
    email = models.EmailField(
        db_column='email',
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Email')
    )

    objects = managers.SubscriberManager()

    class Meta:
        managed = True
        db_table = '"movie"."subscriber"'
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return f'{self.name} - {self.email}'


class SubscriberMovie(ModelBase):
    subscriber = models.ForeignKey(
        to='Subscriber',
        db_column='id_subscriber',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='subscriber_movies'
    )
    movie = models.ForeignKey(
        to='Movie',
        db_column='id_movie',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='subscriber_movies'
    )

    objects = managers.SubscriberMovieManager()

    class Meta:
        managed = True
        db_table = '"movie"."subscriber_movie"'
        verbose_name = _('Subscriber movie')
        verbose_name_plural = _('Subscriber movies')
        indexes = [
            models.Index(fields=['subscriber']),
            models.Index(fields=['movie']),
        ]
        unique_together = (['subscriber', 'movie'])

    def __str__(self):
        return f'{self.subscriber} - {self.movie}'


class Category(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Name')
    )

    objects = managers.CategoryManager()

    class Meta:
        managed = True
        db_table = '"movie"."category"'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f'{self.name}'


class Announcement(ModelBase):
    release_date = models.DateField(
        db_column='release_date',
        null=False,
        blank=False,
        unique=False,
        verbose_name=_('Release date')
    )
    movie = models.ForeignKey(
        to='Movie',
        db_column='id_movie',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='announcements'
    )

    objects = managers.AnnouncementManager()

    class Meta:
        managed = True
        db_table = '"movie"."announcement"'
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')

    def __str__(self):
        return f'{self.movie} - f{self.release_date}'
