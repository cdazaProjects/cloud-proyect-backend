from django.db import models
from customer.models import User
from django.contrib.contenttypes.fields import GenericRelation
from video_encoding.fields import VideoField
from video_encoding.models import Format
from django.core.validators import FileExtensionValidator


# Create your models here.
class Contest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png'])])
    url = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    begin_at = models.DateTimeField('date begin')
    end_at = models.DateTimeField('date end')


class Video(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    file = VideoField(width_field='width', height_field='height', duration_field='duration')
    format_set = GenericRelation(Format)
    status = models.CharField(max_length=50, null=False, default='En Proceso')
    comment = models.CharField(max_length=1000, null=False)
    email = models.EmailField(blank=False, null=False)
    user_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)


class TaskManager(models.Model):
    task_name = models.CharField(max_length=50, null=False)
    begin_at = models.DateTimeField('date begin', auto_now_add=True)
    end_at = models.DateTimeField('date end', null=True)