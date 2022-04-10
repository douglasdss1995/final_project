from rest_framework.routers import DefaultRouter
from movie import viewsets

router = DefaultRouter()
router.register('movie', viewsets.MovieViewSet)
router.register('subscriber', viewsets.SubscriberViewSet)
router.register('subscriber_movie', viewsets.SubscriberMovieViewSet)
router.register('category', viewsets.CategoryViewSet)
router.register('annoucement', viewsets.AnnouncementViewSet)

urlpatterns = router.urls
