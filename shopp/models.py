from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from login.models import Shop , Client
from login.models import User
from django_google_maps import fields as map_fields

#models for category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_re_path(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

def __str__(self):
    return self.user.bizname
#end model category

#product models
class BusinessAddress(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True,default='1')
    businessname = models.CharField(max_length=27, db_index=True)
    building = models.CharField(max_length=18, db_index=True)
    landmark = models.CharField(max_length=20, db_index=True,default='')
    street = models.TextField(max_length=800, db_index=True,default='write the description here...')
    door_no = models.CharField(max_length=10, db_index=True,default='')
    contact = models.CharField(max_length=16, db_index=True,default='')
    floor_no = models.CharField(max_length=10, db_index=True,default='')
    county = models.CharField(max_length=30, db_index=True,choices=(
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
    uniqueadress = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='business/%Y/%m/%d',null=True, blank=True)
    image1 = models.ImageField(upload_to='business/%Y/%m/%d',null=True, blank=True)
    image2 = models.ImageField(upload_to='business/%Y/%m/%d',null=True, blank=True)
    #geolocation = map_fields.GeoLocationField(max_length=100,null=True)
    lat = models.FloatField(max_length=20,null=False,default='-1.2345')
    lon = models.FloatField(max_length=20, null=False,default='36.5432')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-date',)
        
        index_together = (('uniqueadress', 'slug'))

    def __str__(self):
        return self.user.username

    def get_absolute_re_path(self):
        return reverse('shop:business_detail', args=[self.uniqueadress, self.slug])

class ResidentAddress(models.Model):
    building = models.CharField(max_length=30, db_index=True)
    county = models.CharField(max_length=27, db_index=True)
    description = models.CharField(max_length=1000, db_index=True)
    landmark = models.CharField(max_length=30, db_index=True,default='')
    #street = models.CharField(max_length=17, db_index=True,default='')
    door_no = models.CharField(max_length=25, db_index=True,default='')
    floor_no = models.CharField(max_length=25, db_index=True,default='')
    uniqueadress = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    address = map_fields.AddressField(max_length=200,null=True)
    county = models.CharField(max_length=500, db_index=True,choices=(
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
    lat = models.FloatField(max_length=20,null=True,default='-1.2345')
    lon = models.FloatField(max_length=20, null=True,default='36.4567')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username

    def get_absolute_re_path(self):
        return reverse('Profile:detail', args=[self.uniqueadress, self.user])
