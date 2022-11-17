from django import forms
from login.models import User
from shopp.models import BusinessAddress, ResidentAddress



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class ShopCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        #model = Shop
        fields = (
            'shop_name',
            'shop_contact',
            'last_name',
            ' shop_email',
            
        )
    def save(self, commit=True):
        User = super(ShopCreationForm, self).save(commit=False)
        User.shop_name = self.cleaned_data['first_name']
        User.shop_name = self.cleaned_data['last_name']
        User.shop_email = self.cleaned_data['email']

        if commit:
            User.save()

        return User



class BusinessAdressForm(forms.ModelForm):
    
    class Meta:
        model = BusinessAddress
        
        
        fields = [
            #'businessname',
            'category',
            'county',
            'building', 
            'landmark',
            'floor_no',
            'street',
            'door_no',
            'image',
            'image1',
            'image2',
            
            #'contact',
            #'lat',
            #'lon'
            #'geolocation'    
        ]

        
    def save(self, user=None):
        businessname = super(BusinessAdressForm, self).save(commit=False)
        if user:
            businessname.user = user
        businessname.save()
        return businessname


class ResidentAddressForm(forms.ModelForm):
    
    class Meta:
        model = ResidentAddress
        
        
        fields = [
            
            'county',
            'building', 
            'landmark',
            'floor_no',
            'door_no',
            'county',
            'image',
            'description',
            'lat',
            'lon'
            #'geolocation'    
        ]

        
    def save(self, user=None):
        building = super(ResidentAddressForm, self).save(commit=False)
        if user:
            building.user = user
        building.save()
        return building
