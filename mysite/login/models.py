from django.db import models

# Create your models here.
class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Area(models.Model):
    area_name = models.CharField(max_length=200)

    def __str__(self):
        return self.area_name


class Box(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    box_name = models.CharField(max_length=200)
    box_area = models.TextField()

    def __str__(self):
        return self.box_name


class Traffic(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    traffic_name = models.CharField(max_length=200, null=True)
    traffic_image = models.ImageField(null=True, upload_to="images", blank=True)
    traffic_image2 = models.ImageField(null=True, upload_to="images2", blank=True)
    traffic_text = models.CharField(max_length=200, null=True)
    traffic_second = models.IntegerField()
    traffic_second2 = models.IntegerField()




class User(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200, primary_key=True)
    user_pwd = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id