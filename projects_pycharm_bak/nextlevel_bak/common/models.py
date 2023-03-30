from django.db import models
from traffic.models import Area

# Create your models here.
class User(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200, primary_key=True)
    user_pwd = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id