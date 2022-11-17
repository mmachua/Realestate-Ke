from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from login.models import User, Client, Shop
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, UpdateView, CreateView, FormView, DeleteView)
from django.utils.decorators import method_decorator
from shopp.models import Shop
from django.core.paginator import Paginator
from Profile.models import About
from types import MethodType
from operator import attrgetter
#from shopp.forms import ProductForm
from Profile.forms import ShopForm, ClientForm
from login.decorators import shop_required, client_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Friend
from django.urls import reverse_lazy 
from random import randint
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from shopp.models import BusinessAddress

#this is the view that helps users to view shops either theirs or others!!! it has pk that diffrentiates between the two
class ProfileView(TemplateView):
    template_name = 'Profile/Profile.html'
    
    def get(self, request, category_slug=None, pk=None):
        category = None
        context = {}

        if pk:
           
            user = User.objects.get(pk=pk)
            business = BusinessAddress.objects.filter(user=user).order_by('-date')
            print(business)
            
        else:
            category = None
            user = request.user
            business = BusinessAddress.objects.filter(user=request.user.id).order_by('-date')
            print(business)
        args = { 
                 'user' : user,
                  'business' : business,
                 
                 
        }   
          


       
        

   
       
        return render(request, self.template_name, args)

#end view 

#about view
class AboutView(TemplateView):
    template_name = 'Profile/about.html'

    def get(self, request):
        about = About.objects.all()
        
        args = {'about': about}
        return render(request, self.template_name, args)

#end about
 
#view that shows favourite shops
def favouriteshops(request):

    try:
        #users = User.objects.exclude(id=request.user.id)
        users = User.objects.all()
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        users = User.objects.all()
        friends = print("no favourites!!!")

    return render (request, 'Profile/favourites.html', {'users':users,'friends': friends  })

#end view

#view that shows all  shops, this view was originally a class but changed to accomodate pagination which later should be returned to a class
#@login_required
def shop(request, category_slug=None):

    business = BusinessAddress.objects.all()
    paginator = Paginator(business,100)
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page( 1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    index = users.number -1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0 
    end_index = index + 5 if index <=max_index  -5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            #Q(name__icontains=query)|
            Q(shop_name__icontains=query)
            #Q(description__icontains=query)|
            #Q(created__icontains=query)
        )
        users = User.objects.filter(
            Q(is_shop__icontains=query)
        )
    

    return render (request, 'Profile/shop.html', {'business':business,  'page_range': page_range })

#end view
class Product_detailView(TemplateView):
    template_name = 'shop/detail.html'

    def get(self, request, businessname ,pk=None):

        if pk:
            user = User.objects.get(pk=pk)
            business = get_object_or_404(BusinessAddress, user=user,businessname=businessname,  available=True)
        else:
            user = request.user
            business = get_object_or_404(BusinessAddress, id=id, businessname=businessname, available=True) 

        args = {'business': business, 'user': user}
        
        return render(request,self.template_name, args)

#this is the view for the shop admin
@method_decorator([login_required, client_required], name='dispatch')
class ShopadminView(TemplateView):
    template_name = 'Profile/Shopadmin.html'

    def get(self, request,pk=None):
        
        
        context = {}

        if pk:
           
            user = User.objects.get(pk=pk)
            business = BusinessAddress.objects.filter(user=user).order_by('-date')
            
            
        else:
            
            user = request.user
            business = BusinessAddress.objects.filter(user=request.user.id).order_by('-date')
        args = { 
                 'user' : user,
                  'business' : business,
                 
                 
        }   

        return render(request, self.template_name, args)

#end shopadmin view



#view that creates a shop        
@method_decorator([login_required, client_required], name='dispatch')
class ShopFormView(LoginRequiredMixin, CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'Profile/shopform.html'
    success_url = reverse_lazy('Profile:Profile')

    def form_valid(self, form):
        shop_name = form.cleaned_data.get('shop_name')
        description = form.cleaned_data.get('description')
        city = form.cleaned_data.get('city')
        website = form.cleaned_data.get('website')
        phone = form.cleaned_data.get('phone')
        image = form.cleaned_data.get('image')
        #user = form.save()
        form.save(self.request.user)

        return super().form_valid(form)


class ShopFormUpdate(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'Profile/editshop.html'
    success_url = reverse_lazy('Profile:Profile')

    def get_object(self):
        try:
            return self.request.user.shop
        except ObjectDoesNotExist:
            print("hello shop")

    def form_valid(self, form):
        shop_name = form.cleaned_data.get('shop_name')
        description = form.cleaned_data.get('description')
        city = form.cleaned_data.get('city')
        website = form.cleaned_data.get('website')
        phone = form.cleaned_data.get('phone')
        image = form.cleaned_data.get('image')
        form.save(self.request.user)
        return super().form_valid(form)


#view that creates a client userprofile
@method_decorator([login_required, client_required], name='dispatch')
class ClientFormView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'Profile/clientform.html'
    success_url = reverse_lazy( 'login:profile')

#    try:
#        form_class = ClientForm
#    except ObjectDoesNotExist:
#        print("hello")
    def form_valid(self, form):
        
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        image = form.cleaned_data.get('image')
        gender = form.cleaned_data.get('gender')
        user = form.save()
        form.save(self.request.user)

        return super().form_valid(form)
 

#start client update view
"""This is the view for clients that helps them in updating their profiles   """ 
@method_decorator([login_required, client_required], name='dispatch')
class ClientFormUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'Profile/editclient.html'
    success_url = reverse_lazy('login:profile')
    
    def get_object(self):
        try:
            return self.request.user.client
        except ObjectDoesNotExist:
            print ( "hello ")
    
    def form_valid(self, form):
        
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        image = form.cleaned_data.get('image')
        gender = form.cleaned_data.get('gender')
        #user = form.save()
        form.save(self.request.user)
        messages.success(self.request, 'The update was done successfully!!!')

        return super().form_valid(form)

#end client update view

