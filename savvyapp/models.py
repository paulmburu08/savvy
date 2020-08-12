from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from tinymce.models import HTMLField

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = HTMLField()
    email = HTMLField()
    location = HTMLField('Location/Neighborhood')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Businesses(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class Posts(models.Model):
    image = CloudinaryField('image')
    title = HTMLField()
    description = HTMLField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

