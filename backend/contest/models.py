from django.db import models
from customer.models import User

# Create your models here.
class Contest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='images/', max_length=100)
    url = models.CharField(max_length=100)
    description = models.TextField()
    begin_at = models.DateTimeField('date begin')
    end_at = models.DateTimeField('date end')

class Video(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)