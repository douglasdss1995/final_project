from rest_framework import serializers

from movie import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriber
        fields = '__all__'


class SubscriberMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriberMovie
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Announcement
        fields = '__all__'
