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
