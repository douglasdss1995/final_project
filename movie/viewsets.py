from rest_framework import viewsets

from movie import models, serializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = models.Subscriber.objects.all()
    serializer_class = serializers.SubscriberSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class SubscriberMovieViewSet(viewsets.ModelViewSet):
    queryset = models.SubscriberMovie.objects.all()
    serializer_class = serializers.SubscriberMovieSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)
