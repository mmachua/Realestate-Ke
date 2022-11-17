from django import forms
from login.models import User, Shop, Client
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#the models for these forms are in login.// rhis form has been put here as an extension
class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop

        fields = [
            
            
            'Industry',
            'description',
            'county',
            'building',
            
            'phone',
            'image',
            'street',
        ]

    def save(self, user=None):
        shop = super(ShopForm, self).save(commit=False)
        if user:
            shop.user = user
        shop.save()
        return shop




class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
       # model = User

        fields = [
            
            'phone',
            'county',
            'image',
            'street',
            'building',
            
        ]

    def save(self, user=None):
        client = super(ClientForm, self).save(commit=False)
        if user:
            client.user = user
        client.save()
        return client



