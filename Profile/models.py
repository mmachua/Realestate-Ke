from __future__ import unicode_literals
#from django.core.urlresolvers import reverse
from django.db import models
from login.models import User
from login.models import Shop, Client
#from django.contrib.auth import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse



class About(models.Model):
    logo = models.ImageField(null=True, blank=True)
    text = models.TextField(max_length=1500,null=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Aboutpage(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image =models.ImageField(upload_to='post/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='post/%Y/%m/%d', blank=True)

    aboutus = models.TextField(max_length=500, blank=True)
    aboutimage = models.ImageField(upload_to='post/%Y/%m/%d', blank=True)

    story = models.TextField(max_length=1500, blank=True)
    storyimage = models.ImageField(upload_to='post/%Y/%m/%d', blank=True)

    team = models.TextField(max_length=1500, blank=True)
    teamimage = models.ImageField(upload_to='post/%Y/%m/%d', blank=True)
    whyus = models.TextField(max_length=1500, blank=True)
    whyusimage = models.URLField(max_length=350, blank=True)

    def __str__(self):
        return self.title

    