from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    installed_apps = models.IntegerField(default=0)
    storage_used = models.FloatField(default=0.0)  # بر حسب مگابایت
    last_login_time = models.DateTimeField(auto_now=True)
    battery_level = models.IntegerField(default=100)
    internet_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
