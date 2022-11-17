
from __future__ import unicode_literals
from django.db import models
from login.models import User
from login.models import Shop, Client
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django_google_maps import fields as map_fields
#from django.contrib.gis.geos import GEOSGeometry
#from django.contrib.gis.db import models
#from django.contrib.gis.db.models import PointField
#from leaflet.admin import LeafletGeoAdmin

class Coordenadas(models.Model):

    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    #mpoint = models.PointField()
    #coordinate = models.PointField(blank=True, null=True)



class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    
class Post(models.Model):
    post = models.CharField(max_length=500)
    image = models.URLField(max_length=350, blank=True)
    imagedescription = models.CharField(max_length=500, blank=True)

    image1 = models.URLField(max_length=350, blank=True)
    imagedescription1 = models.CharField(max_length=500, blank=True)
    post1 = models.CharField(max_length=500, blank=True)

    image2 = models.URLField(max_length=350, blank=True)
    imagedescription2 = models.CharField(max_length=500, blank=True)
    post2 = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.post


class Homepage(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=700,blank=True)
    image = models.URLField(max_length=350, blank=True)

    title1 = models.CharField(max_length=500)
    content1 = models.CharField(max_length=700, blank=True)
    image1 = models.URLField(max_length=350, blank=True)
 
    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

#this model help in storing and remooving favourite shops
class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="owner", null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend,created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
    
    def __str__(self):
        return str(self.current_user)

    def user(self):
        return self.users.count()

#end view

#contact mmodel helps clients and shops to contact Favourite
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#privacy model
class Privacy(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=7000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Terms(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#about

class Aboutpage(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    aboutus = models.TextField(max_length=500, blank=True)
    aboutimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    project = models.TextField(max_length=500, blank=True)
    projectimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    story = models.TextField(max_length=1500, blank=True)
    storyimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    team = models.TextField(max_length=1500, blank=True)
    teamimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    whyus = models.TextField(max_length=1500, blank=True)
    whyusimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
