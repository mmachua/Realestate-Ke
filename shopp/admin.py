from django.contrib import admin
from .models import Category
# Register your models here.
from .models import BusinessAddress, ResidentAddress

class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','slug','user']
    prepopulated_fields = {'slug': ('name','user')}
admin.site.register(Category, CategoryAdmin)

class BusinessAddressAdmin(admin.ModelAdmin):
    list_display = ['businessname',  'building', 'county','uniqueadress','lat','lon','user']
    list_filter = [ 'county']
   
admin.site.register(BusinessAddress, BusinessAddressAdmin)
 
class ResidentAddressAdmin(admin.ModelAdmin):
    list_display = [  'building', 'county','uniqueadress','lat','lon','user']
    list_filter = [ 'county']
admin.site.register(ResidentAddress, ResidentAddressAdmin)