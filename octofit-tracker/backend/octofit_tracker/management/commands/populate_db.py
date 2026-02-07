from django.core.management.base import BaseCommand
from django.db import connection
from djongo import models

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=255)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    suggested_for = models.CharField(max_length=255)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user_email='ironman@marvel.com', activity_type='Running', points=50),
            Activity(user_email='captain@marvel.com', activity_type='Cycling', points=40),
            Activity(user_email='spiderman@marvel.com', activity_type='Swimming', points=30),
            Activity(user_email='batman@dc.com', activity_type='Running', points=60),
            Activity(user_email='superman@dc.com', activity_type='Cycling', points=70),
            Activity(user_email='wonderwoman@dc.com', activity_type='Swimming', points=80),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=210)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes.', suggested_for='Marvel'),
            Workout(name='Justice Yoga', description='Yoga for balance and strength.', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create unique index on email for users
        with connection.cursor() as cursor:
            cursor.execute('CREATE INDEX IF NOT EXISTS email_unique_idx ON octofit_tracker_user (email)')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
