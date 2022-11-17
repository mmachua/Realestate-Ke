from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import RegistrationForm
#from login.forms import ( EditProfileForm)
#from django.contrib.auth.models import User
from ..models import User
from shopp.models import ResidentAddress
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm#, EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from login.forms import  EditProfileForm#, contactForm
#from home.views import Post
from home.models import  Friend
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
#from login.models import UserProfile
#from shopp.models import Product, Category

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template




class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def home(self, request):
        if request.user.is_authenticated:
            if request.user.is_shop:
                return redirect('shopp:product_list')
            else:

            
                return redirect('shop:product_list')
            if request.user.is_client:

                return redirect('shopp:product_list')
            
            else:
                return redirect('shop:product_list')
        
        return render(request,'login/home.html')

#    def get(self, request):
#        if request.user.is_authenticated:
#            if request.user.is_client:
##                return redirect('shopp:product_list')
 #           else:
#                return redirect('shopp:product_list')
#        return render(request,'registration/signup.html')




@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'login/profile.html'
    
    def get(self, request,category_slug=None, pk=None):
       

        if pk:
            users = User.objects.exclude(id=request.user.id)
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
            resident = ResidentAddress.objects.filter(current_user=request.user).order_by('-date')
            print(resident)
        else:
            users = User.objects.all()
            friends = Friend.objects.all()
            resident = ResidentAddress.objects.filter(user=request.user).order_by('-date')
            print(resident)
        args = {
                 'resident': resident,
                 'users': users,
         'friends': friends
        }
        return render(request, self.template_name, args)

    




@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'login:profile' )

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
        
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user )

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect( 'login:profile' )

        else:
            return redirect('/login/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)




def about(request):
    context = locals()
    #template = 'about.html'
    #form = contactForm(request.POST or None)
#
#    if form.is_valid():
#        print( request.POST)
#        context = locals()
    return render(request, 'login/about.html')#,context )
 


@login_required
def login_admin(request):
    return render(request, 'admin/login.html')


@login_required
def delete_user(request, username):
    context = {}
    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = 'The user is deleted.'       
    except User.DoesNotExist: 
        context['msg'] = 'User does not exist.'
    except Exception as e: 
        context['msg'] = e.message

    return render(request, 'template.html', context=context) 

