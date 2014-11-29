from django.db import models

class Streak(models.Model):
	activity = models.CharField(max_length=120)
	current_streak = models.IntegerField(default=0)
	longest_streak = models.IntegerField(default=0)
