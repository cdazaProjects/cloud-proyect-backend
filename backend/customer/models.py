from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer")    

    def __str__(self):
        return self.user

# Signal (For user inherited model "customer" creation)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        customer.objects.create(user=instance)


class Contest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
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