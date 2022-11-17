from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from estate import settings
from django.db.models.signals import post_save
import uuid
from django.db import models
#from django_google_maps import fields as map_fields

class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_shop = models.BooleanField(default=False)


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Industry = models.CharField(max_length=21, default='',choices=(
                                    ('Real Estate', 'Real Estate'),
                                    
                                    ('Technology', 'Technology'),
                                    ('Botique', 'Botique'),
                                    ('Second Hand Items', 'Second Hand Items'),
                                    ('Transport', 'Transport'),
                                    ('Insuarance', 'Insuarance')))
    description = models.CharField(max_length=100, default='')
    county = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    building = models.CharField(max_length=21, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True, default='0')
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    
    phone = models.IntegerField(default=0)
    county = models.CharField(max_length=100,blank=True, null=True, default='',choices=(
                                   ('Mombasa', 'Mombasa'),
                                    ('Nairobi', 'Nairobi'),
                                    ('Kwale', 'Kwale'),
                                    ('Kilifi', 'Kilifi'),
                                    ('Tana-River', 'Tana-River'),
                                    ('Lamu', 'Lamu'),
                                    ('Meru', 'Meru'),
                                    ('Embu', 'Embu'),
                                    ('Garissa', 'Garissa'),
                                    ('Lamu', 'Lamu'),
                                    ('Kitui', 'Kitui'),
                                    ('Machakos', 'Machakos'),
                                    ('Makueni', 'Makueni'),
                                    ('Nyandarua', 'Nyandarua'),
                                    ('Nyeri', 'Nyeri'),
                                    ('Kirinyaga', 'Kirinyaga'),
                                    ('Murang’a', 'Murang’a'),
                                    ('Kiambu', 'Kiambu'),
                                    ('Trans-Nzoia', 'Trans-Nzoia'),
                                    ('Uasin-Gishu', 'Uasin-Gishu'),
                                    ('Laikipia', 'Laikipia'),
                                    ('Narok', 'Narok'),
                                    ('Kajiado', 'Kajiado'),
                                    ('Kericho', 'Kericho'),
                                    ('Bomet', 'Bomet'),
                                    ('Kisumu', 'Kisumu'),
                                    ('Kisii', 'Kisii'),
                                    ('Nyamira', 'Nyamira'),
                                    ('HomaBay', 'HomaBay'),
                                    ('Baringo', 'Baringo'),
                                    ('Samburu', 'Samburu'),
                                    ('Taita-Taveta', 'Taita-Taveta'),
                                    ('Wajir', 'Wajir'),
                                    ('Mandera', 'Mandera'),
                                    ('Marsabit', 'Marsabit'),
                                    ('Isiolo', 'Isiolo'),
                                    ('Tharaka-Nithi', 'Tharaka-Nithi'),
                                    ('Turkana', 'Turkana'),
                                    ('West-Pokot', 'West-Pokot'),
                                    ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
                                    ('Nandi', 'Nandi'),
                                    ('Kakamega', 'Kakamega'),
                                    ('Vihiga', 'Vihiga'),
                                    ('Bungoma', 'Bungoma'),
                                    ('Busia', 'Busia'),
                                    ('Siaya', 'Siaya'),
                                    ('Migori', 'Migori'),
                                    ('Nakuru', 'Nakuru')))
    image = models.ImageField(upload_to='profile_image', blank=False ,default='')
    street = models.CharField(max_length=21, default='')
    building = models.CharField(max_length=21, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.username

