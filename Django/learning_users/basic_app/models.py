from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User) #extends User class to add to it

    #additional classes
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) #need to pip install pillow to support images

    def __str__(self):
        return self.user.username
