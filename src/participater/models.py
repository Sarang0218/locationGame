from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
import hashlib

class Location(models.Model):
  
  player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
  )
  lat = models.FloatField(default=0)
  long = models.FloatField(default=0)
  time = models.DateTimeField(default=timezone.now)

  def __str__(self):
    dat = hashlib.sha224(f"{self.lat}, {self.long}".encode()).hexdigest()
    return f"({dat}) {self.player.username}"
class Player(models.Model):
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
  )
  hunter = models.BooleanField()
  def __str__(self):
    return self.user.username
  