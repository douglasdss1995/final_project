from django.contrib import admin

from movie import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'modified_at', 'active']
    list_display_links = ['id', 'title', 'modified_at', 'active']
    search_fields = ['title']
    list_filter = ['active']


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'modified_at', 'active']
    search_fields = ['name']
    list_filter = ['active']


@admin.register(models.SubscriberMovie)
class SubscriberMovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'modified_at', 'active']
    list_display_links = ['id', 'modified_at', 'active']
    list_filter = ['active']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'modified_at', 'active']
    search_fields = ['name']
    list_filter = ['active']


@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'modified_at', 'active']
    list_display_links = ['id', 'modified_at', 'active']
    list_filter = ['active']
