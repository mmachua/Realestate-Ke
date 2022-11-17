

from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
#from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from login.models import User
#from home.forms import HomeForm, HomeCreate
#from home.models import Post, Friend
#from .models import Create
from home.forms import ContactForm, NewsletterForm
from home.models import Contact, Privacy, Terms, Aboutpage
from login.models import Client, Shop
from .models import Friend, Post, Newsletter
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy
from random import randint
from home.models import Post, Homepage, Aboutpage
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from shopp.models import BusinessAddress
#from geopy.geocoders import Nominatim
import folium
import pandas as pd
#from folium import plugins
#gee
#import ee
#service_account = ' residentgeolocate@resident-350617.iam.gserviceaccount.com'
#credentials = ee.ServiceAccountCredentials(service_account, 'home\private.json')
#ee.Initialize(credentials)
import folium
from home.forms import CoordinatesForm
from .models import Coordenadas
from shopp.models import BusinessAddress

def coordinates_form(request):
    coordinates = Coordenadas.objects.all()
    form = CoordinatesForm()

    #if request.method == 'POST':
        #form = CoordinatesForm(request.POST)
        #if form.is_valid():
        #    form.save()
    #    return redirect("maps")
    context = {
        'coordinates': coordinates,
            #'form' : form,
    }
    return render(request, 'home/mapss.html', context)

def maps(request):
    business = BusinessAddress.objects.all().values()
    coordenadas = list(BusinessAddress.objects.values_list('lat','lon'))#
    cod = pd.DataFrame(business)
   
    #print(coordenadas)
    map = folium.Map(location=[cod.lat.mean(), cod.lon.mean()], zoom_start=13, control_scale=False)
    for index, location_info in cod.iterrows():
        folium.Marker([location_info["lat"], location_info["lon"]], popup=(location_info['businessname'], location_info['building'])).add_to(map)
    
    

    map = map._repr_html_()
    context = {
        'map': map, 'business': business

        }
    return render(request, 'home/map.html', context)

from .mixins import Directions
'''
Basic view for routing 
'''


@login_required
def home(request):
    return render(request, 'core/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'
    model = Newsletter
    form_class = NewsletterForm

    def get(self, request):
        form = NewsletterForm()
        posts = Post.objects.all()
        homepages = Homepage.objects.all() 

        args = {
            'posts': posts, 'homepages': homepages, 'form': form
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.user = request.user
            newsletter.save()
            title = 'Thanks!!'
            confirm_message = "Thankyou for subscribing to our newsletter, Email received"
            context = {'title': title, 'confirm_message': confirm_message }
            
        return render(request, self.template_name, context)


@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
        return redirect('Profile:shop')
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('Profile:favouriteshops') 



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('shopp:product_list')

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Thanks!!'
            confirm_message = 'Thanks for the message. We will get right back to you!'
            context = {'title': title, 'confirm_message': confirm_message}
        return render(request, self.template_name, context)
        #return redirect('shopp:product_list')



class PrivacyView(TemplateView):
    template_name = "home/privacy.html"

    def get(self, request):
        #form = PrivacyForm()
        privacy = Privacy.objects.all()#.order_by('-date')

        args = {'privacy': privacy }
        return render(request, self.template_name, args)

    def post(self, request):
        form = PrivacyForm()
        if form.is_valid():
            #privacy = form.save(commit=False)
            privacy = get_object_or_404(Privacy, id=id, slug=slug)
            privacy.user = request.user
            privacy.save()
            return redirect('home:privacy')
        args = {'privacy':privacy }
        return render(request, self.template_name, args)   


class TermsView(TemplateView):
    template_name = 'home/terms.html'

    def get(self, request):
        terms = Terms.objects.all()
        args = {'terms':terms }
        return render(request, self.template_name, args)

    def post(self, request):
        if form.is_valid():
            terms = get_object_or_404(Terms)
            terms.user = request.user
            terms.user()
            return redirect('home:terms')

        args = {'terms':terms}
        return render(request, self.template_name, args)

class AboutView(TemplateView):
    template_name = 'home/about.html'


    def get(self, request):
        aboutpages = Aboutpage.objects.all()

        args = {
            'aboutpages': aboutpages
        }
        return render(request, self.template_name, args)

#class MarkersMapView(TemplateView):
#    template_name = 'index.html'

    # Define a method for displaying Earth Engine image tiles on a folium map.
    #def get_context_data(self, **kwargs):

#        figure = folium.Figure()
        
        #create Folium Object
#        m = folium.Map(
#            location=[28.5973518, 83.54495724],
#            zoom_start=8
#        )

        #add map to figure
#        m.add_to(figure)

        
        #select the Dataset Here's used the MODIS data
#        dataset = (ee.ImageCollection('MODIS/006/MOD13Q1')
#                  .filter(ee.Filter.date('2019-07-01', '2019-11-30'))
#                  .first())
#        modisndvi = dataset.select('NDVI')

        #Styling 
#        vis_paramsNDVI = {
#            'min': 0,
#            'max': 9000,
#            'palette': [ 'FE8374', 'C0E5DE', '3A837C','034B48',]}

        
        #add the map to the the folium map
#        map_id_dict = ee.Image(modisndvi).getMapId(vis_paramsNDVI)
       
        #GEE raster data to TileLayer
#        folium.raster_layers.TileLayer(
#                    tiles = map_id_dict['tile_fetcher'].url_format,
#                    attr = 'Google Earth Engine',
#                    name = 'NDVI',
#                    overlay = True,
#                    control = True
#                    ).add_to(m)

        
        #add Layer control
#        m.add_child(folium.LayerControl())
       
        #figure 
#        figure.render()
         
        #return map
        #return {"map": figure}


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "home/map.html"

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('Profile:shop')