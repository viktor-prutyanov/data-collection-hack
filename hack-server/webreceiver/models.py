from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class Reports(models.Model):
	user_id = models.IntegerField(default=0, primary_key=True)
	lat = models.FloatField(default=0)
	lng = models.FloatField(default=0)
	time = models.DateTimeField(default=timezone.now)
	presence = models.BooleanField(default=False)
	name = models.TextField(default="")

# Create your models here.
