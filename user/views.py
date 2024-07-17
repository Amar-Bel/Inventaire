from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
              username=form.cleaned_data.get('username')
              messages.success(request,f'Un compte a été créé pour {username}.Continuer à vous connecter')
              form.save()
              return redirect('user-login')
    else :
         form =  CreateUserForm()
    context = {
        'form' : form
         }
    return render(request, 'user/register.html',context)

# Create your views here.
def custom_logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')


def profile(request):
    # Ajoutez votre logique de traitement iciè x
    context = {
        'user': request.user,
        # Ajoutez d'autres données de contexte ici
    }
    return render(request, 'user/profile.html', context)

def profile_update(request):
    if request.method =='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profil_form=ProfileUpdateForm(request.POST,request.FILES , instance=request.user.profile)
        if user_form.is_valid() and profil_form.is_valid():
            user_form.save()
            profil_form.save()
            return redirect('user-profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profil_form=ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'user_form':user_form,
        'profile_form':profil_form,

    }
     
    return render(request,'user/profile_update.html',context)