from django.conf.urls import url
from django.urls import include, re_path
#from home.views import 
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from home import views
from . import views 
from home.views import ContactView, PrivacyView, TermsView, MarkersMapView, AboutView, HomeView, coordinates_form, maps #, map, route


app_name = 'home'


urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^privacy/', PrivacyView.as_view(), name='privacy' ),
    re_path(r'^terms/', TermsView.as_view(), name='terms'),
    #re_path(r"^map/", MarkersMapView.as_view(),name="map"),
    #re_path(r'^route/', views.route, name="route"),
    re_path(r'^coordinates-form/',views.coordinates_form, name = 'coordinates-form'),
    re_path(r'^map/', views.maps, name="map"),
    
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', 
            views.change_friends, name='change_friends'),
    re_path('contact/', ContactView.as_view(), name='Contact'),
    re_path(r'^about/', AboutView.as_view(), name='about'),

  
]


