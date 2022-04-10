import yagmail

from movie import models


class AnnouncementActions:
    @staticmethod
    def send_announcement(announcement: 'models.Announcement'):
        movie = announcement.movie

        message = f"""
        The movie {movie.title} will be released in {announcement.release_date}
        """

        subscribers = models.Subscriber.objects.filter(
            subscriber_movies__movie__id=movie.id
        )

        for subscriber in subscribers:
            yag = yagmail.SMTP(
                'username',
                'password'
            )
            yag.send(
                # to=subscriber.email,
                to=subscriber.email,
                subject=message,
                contents=message,
            )
