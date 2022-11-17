from django.shortcuts import render
from estate import settings
from login.decorators import shop_required, client_required
from django.views.generic import (ListView, UpdateView, CreateView, FormView, DeleteView)
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from shopp.models import Category# Product 
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q
from login.models import User 
from shopp.forms import BusinessAdressForm ,ResidentAddressForm#,ShopCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from home.models import Friend
from django.contrib.auth.mixins import LoginRequiredMixin
from shopp.models import BusinessAddress,ResidentAddress
from django.urls import reverse_lazy


def all_shops(request):
    #args = {'user': request.user}
    return HttpResponse('kdkdl')



## this is the view to the shop don't edit  ##
#@login_required
def product_list(request, category_slug=None ,pk=None):
    
    category = None
    categories = Category.objects.all()
    business = BusinessAddress.objects.all()
    users = User.objects.exclude(id=request.user.id).order_by('date_joined')

    query = request.GET.get('q')
    if query:
        business = BusinessAddress.objects.filter(
            Q(businessname__icontains=query)|
            Q(building__icontains=query)|
            Q(street__icontains=query)|
            Q(county__icontains=query)
        )
        users = User.objects.filter(
            Q(is_shop__icontains=query)
        )
    else:
        business = BusinessAddress.objects.all()

    

#    friend = Friend.objects.get(current_user=request.user)
#    friends = friend.users.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        #products = products.filter(category=category)
        business = BusinessAddress.filter(category=category)
    
    paginator = Paginator(business,44)
    page = request.GET.get('page')
    try:
        business = paginator.page(page)
    except PageNotAnInteger:
        business = paginator.page(1)
    except EmptyPage:
        business = paginator.page(paginator.num_pages)
    index = business.number -1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0 
    end_index = index + 5 if index <=max_index  -5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    #paginator = Paginator(users, 14)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)

    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    index = users.number -1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0 
#    end_index = index + 5 if index <=max_index  -5 else max_index
#    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'shop/list.html',{'category': category,
    'categories':categories, 'business': business ,'users': users  ,# 'friends': friends,
     'page_range': page_range })

#end of shop view


#@method_decorator(login_required, name='dispatch')
class Product_detailView(TemplateView):
    template_name = 'shop/detail.html'

    def get(self, request, uniqueadress , slug ,pk=None):

        if pk:
            user = User.objects.get(pk=pk)
            business = get_object_or_404(BusinessAddress,businessname=businessname, slug=slug, uniqueadress=True)
        else:
            user = request.user
            business = get_object_or_404(BusinessAddress, uniqueadress=uniqueadress) 

        args = {'business': business, 'user': user }
        
        return render(request,self.template_name, args) 
                
class Resident_detailView(TemplateView):
    template_name = 'Profile/detail.html'

    def get(self, request, uniqueadress , date ,pk=None):

        if pk:
            user = User.objects.get(pk=pk)
            resident = get_object_or_404(ResidentAddress,uniqueadress=uniqueadress, user=user)
        else:
            user = request.user
            resident = get_object_or_404(ResidentAddress, uniqueadress=uniqueadress) 

        args = {'resident': resident, 'user': user }
        
        return render(request,self.template_name, args) 
      

class Contactview(TemplateView):
    template_name = 'shop/contact_us.html'


def contact_us(request):
    form_class = ContactForm(request.POST or None)

    return render(request, 'shop/contact_us.html', {
        'form': form_class,
    })


def AbouttView(request):
 #   #args = {'user': request.user}
    return render(request,('shop/about_uss.html'))   

def registershop(request):
    if request.method == 'POST':
        form = ShopCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop/shopp')
        else:
            form = ShopCreationForm()

           # args = ('form': form)
            return render(request, 'shop/reg_form.html')#, args)




def search(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'shop/search/product_list.html', {'filter': product_filter})

class ShopsView(TemplateView):
    template_name = 'shop/shops.html'
    

    def get(self, request):
        
        
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        query = request.GET.get('q')
        if query:

            users = User.objects.filter(
            Q(shop_name__icontains=query)#|
#            Q(user__username__icontains=query)|
#            Q(description__icontains=query)|
            #Q(created__icontains=query)
        )


        args = {  'users': users,
         'friends': friends
        }
        return render(request, self.template_name, args)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "shop/product_delete.html", context)




def delete_view(request, id):
    item_to_delete = Product.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('/')



#@method_decorator([login_required, shop_required], name='dispatch')
class BusinessAdressFormView(LoginRequiredMixin, CreateView):
    model = BusinessAddress
    form_class = BusinessAdressForm
    template_name = 'shop/businessadress_form.html'
    success_url = reverse_lazy('Profile:Shopadmin')

 
    def form_valid(self, form):
       
        businessname = form.cleaned_data.get('name')
        building = form.cleaned_data.get('building')
        image = form.cleaned_data.get('image')
        county = form.cleaned_data.get('county')
        
        form.save(self.request.user)
        return super().form_valid(form)


#@method_decorator([login_required, shop_required], name='dispatch')
class ResidentAddressFormView(LoginRequiredMixin, CreateView):
    model = ResidentAddress
    form_class = ResidentAddressForm
    template_name = 'shop/residentadressform.html'
    success_url = reverse_lazy('login:profile')

 
    def form_valid(self, form):
       
        businessname = form.cleaned_data.get('name')
        building = form.cleaned_data.get('building')
        image = form.cleaned_data.get('image')
        county = form.cleaned_data.get('county')
        
        form.save(self.request.user)
        return super().form_valid(form)
