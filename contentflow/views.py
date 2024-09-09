from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, View

from . import forms


# Create your views here.
class TestView(View):
    def get(self, request):
        form =  forms.PublicationForm(initial={'user': request.user})
        
        context = {
            'form': form,
        }
        return render(request, 'test.html', context)
    
    def post(self, request):
        form =  forms.PublicationForm(request.POST or None, initial={'user': request.user})
        form.user = request.user
        context = {
                'form': form,
            }
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            form.save_m2m()
            
            
            return render(request, 'test.html', context)
        return render(request, 'test.html', context)
    
class UserProfileView(View):
    
    def get(self, request):
        context = {
            'profile_form': forms.UserProfileForm(instance=request.user.profile),
            'user_form': forms.UserChangeForm(instance=request.user)
        }
        return render(request, 'auth/user-change.html', context)
    
    def post(self, request):
        
        profile_form = forms.UserProfileForm(request.POST or None, instance=request.user.profile)
        user_form = forms.UserChangeForm(request.POST or None, instance=request.user)
        
    
        
        if profile_form.is_valid() and user_form.is_valid() :
            
            profile = profile_form.save(commit=False)
            #profile.user = request.user 
            profile.save()
            
            user = user_form.save(commit=False)
            user.user = request.user
            user.save()
            messages.success(request, 'The user information has been updated successfully.')
            return redirect(reverse('user-change')) 
        
        context = {
            'profile_form': forms.UserProfileForm(instance=request.user.profile),
            'user_form': forms.UserChangeForm(instance=request.user)
        }
           
        return render(request, 'auth/user-change.html', context)

            