
from django.contrib import admin
from home.models import Friend
from .models import Contact, Privacy , Terms
#from django.contrib.gis import admin
from .models import Post, Homepage, Aboutpage, Newsletter, Rental, Coordenadas
from .models import Contact
# Register your models here.

#admin.site.register(Post)
#admin.site.register(Homepage)
#dmin.site.register(Aboutpage)
#admin.site.register(Newsletter)
admin.site.register(Rental)
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

#admin.site.register(Coordenadas)

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content','user']
admin.site.register(Contact, ContactAdmin)


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Privacy, PrivacyAdmin)


class TermsAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Terms, TermsAdmin)