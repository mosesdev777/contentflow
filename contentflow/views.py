import os
import stat
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile

from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import (Publication, Channel, SocialMedia, VoiceAuthor, Subcription, Planning,
                     Account, Book, Phrase, Prompt,Title , Character, Hook)
from . import forms


class HomeView(TemplateView):
    template_name = 'home.html'
class AboutView(TemplateView):

    template_name = 'about.html'

class ContactView(View):
    template_name = 'contact.html'
    
    def get(self, request, *args, **kwargs):
        
        form = forms.ContactForm()
        context = {
            'form': form
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = forms.ContactForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
        

# Create your views here.

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class PublicationListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/publications/index.html'
    queryset = Publication.objects.all()
    paginate_by = 10
    context_object_name = 'publications'
 
class PublicationDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'auth/publications/detail.html'
    

    def get(self, request, uuid):
        publication = get_object_or_404(Publication, uuid=uuid)
        
        context = {
            "publication": publication, 
            "url": "publications"
        }
        
        return render(request, self.template_name, context)
     
    
class PublicationCreateView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        form = forms.PublicationForm(initial={'user': request.user})
        
        context = {
            'form': form,
        }
        return render(request, 'auth/publications/create.html', context)
    
    def post(self, request):
        form = forms.PublicationForm(request.POST or None, initial={'user': request.user})
        form.user = request.user
        context = {
                'form': form,
            }
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            form.save_m2m()
            
            messages.success(request, 'Publication created successfully')
            
            return redirect('publications')
            
        return render(request, 'auth/publications/create.html', context)
    
class UpdatePublicationView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, uuid):
        publication =  get_object_or_404(Publication, uuid=uuid)
        form = forms.PublicationForm(instance=publication)
        return render(request, 'auth/publications/update.html', {'form': form, 'uuid': uuid})
    
    def post(self, request, uuid):
        publication =  get_object_or_404(Publication, uuid=uuid)
        form = forms.PublicationForm(request.POST, instance=publication)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Publication was updated successfully')
            return render(request, 'auth/publications/update.html', {'form': form, 'uuid': uuid})
        return render(request, 'auth/publications/update.html', {'form': form, 'uuid': uuid})

class DeletePublication(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def post(self, request, uuid):
        publication = get_object_or_404(Publication, uuid=uuid)
        publication.delete()
        messages.success(request, 'The publication was deleted successfuly')
        return redirect('publications')
        

class UserProfileView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    
    template_name = 'auth/profile/index.html'
    def get_queryset(self, *args, **kwargs):
        user = User.objects.filter(id=self.request.user.id)
        return user
    context_object_name = "user"

class UserProfileChangeView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'auth/profile/update.html'
    
    def get(self, request, pk):
        
        user_change_form = forms.UserChangeForm(instance=request.user)
        user_profile_form = forms.UserProfileForm(instance=request.user)
        
        context = {
            'user_form': user_change_form,
            'profile_form': user_profile_form, 
        }
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        
        profile = get_object_or_404(Profile, user=request.user)
        user_change_form = forms.UserChangeForm(request.POST, instance=request.user)
        user_profile_form = forms.UserProfileForm(request.POST, request.FILES, instance=profile)
        
        context = {
            'user_form': user_change_form,
            'profile_form': user_profile_form, 
        }
        
        
        if 'user_info' in request.POST:
            if user_change_form.is_valid():
                user_change_form.save()
                messages.success(request, 'User profile updated successfully')    
                return redirect('profile-change', request.user.pk)
            
        
        elif 'profile_info' in request.POST:
            if user_profile_form.is_valid():
                user_profile_form.save(commit=False)
                profile = Profile.objects.get(user=request.user)
                new_avatar = request.FILES.get('avatar')
                
                folder = os.path.join(settings.BASE_DIR, 'media')
                old_avatar = profile.avatar
                
                print(folder)
                
                
                    
                if new_avatar:
                    try:
                        os.remove(f"{folder}/{old_avatar}")
                    except:
                        print("image does not exist")    
                    user_profile_form.save()
                    messages.success(request, 'User avatar updated successfully')    
                    return redirect('profile-change', request.user.pk)
                else:
                    messages.info(request, 'No avatar was sent')    
                    return redirect('profile-change', request.user.pk)
                
        
        else:
            messages.success(request, 'Something went wrong, please try again')    
            return redirect('profile-change', request.user.pk )
        

class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'auth/profile/delete.html'
    model = User 
    success_url =  '/login/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Your account has been deleted successfully')
        return super().form_valid(form)
                     
class LoginView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect(reverse('dashboard'))

        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(sefl, request):
        form = forms.LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))
                
            else:
                form = forms.LoginForm()
                messages.error(request, 'Username or passsword invalid')
                return render(request, 'login.html', {'form': form})
        
        else:
            form = forms.LoginForm()
            messages.error(request, 'All fiels are required')
            return render(request, 'login.html', {'form': form})
class RegisterView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect(reverse('dashboard'))
        
        form = forms.RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = forms.RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))

        else:
            form = forms.RegisterForm(request.POST)
            return render(request, 'register.html', {'form': form})        

class DashboardView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/dashboard.html'
    queryset = Publication.objects.all().order_by('-id')[0:5]
    context_object_name = 'posts'
          

class ChannelListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/channels/index.html'
    context_object_name = 'channels'
    paginate_by = 10
    queryset = Channel.objects.all().order_by('-id')
class CreateChannelView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = forms.ChannelForm()
        return render(request, 'auth/channels/create.html', {'form':form })            
    
    def post(self, request):
        form = forms.ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Channel created successfuly')
            return redirect('channels')
        
        form = forms.ChannelForm(request.POST)
        return render(request, 'auth/channels/create.html', {'form':form }) 
         
class UpateChannelView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = forms.ChannelForm
    template_name = 'auth/channels/update.html'
    model = Channel
    success_url = reverse_lazy('channels')
    
    def form_valid(self, form):
        messages.success(self.request, 'Channel was updated successfully')
        return super().form_valid(form)

class DeleteChannelView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('channels')
    model = Channel
    template_name = 'auth/channels/delete.html'
    context_object_name = 'channel'
    
    def form_valid(self, form):
        messages.success(self.request,'Channel deleted successfully')
        return super().form_valid(form)
        
                

class SocialMediaView(LoginRequiredMixin, ListView):  
    template_name = 'auth/social-medias/index.html'
    queryset = SocialMedia.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'social_medias' 
class CreateSocialMediaView(LoginRequiredMixin, CreateView):
    
    template_name = 'auth/social-medias/create.html'
    form_class = forms.SocialMediaForm
    success_url = '/social-medias/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Social media was created successfully')
        return super().form_valid(form)
    
    

class UpdateSocialMediaView(LoginRequiredMixin, UpdateView):
    
    template_name = 'auth/social-medias/update.html'
    model = SocialMedia
    form_class = forms.SocialMediaForm
    context_object_name = 'social_media'
    success_url = '/social-medias/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Social media was updated successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.info(self.request, 'Please correct the info below')
        return super().form_invalid(form)
        

    
class DeleteSocialMediaView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'auth/social-medias/delete.html'
    context_object_name = 'social_media'
    success_url = '/social-medias/'
    model = SocialMedia 
    
    def form_valid(self, form):
        messages.success(self.request, 'Social media deleted successfully')
        return super().form_valid(form)   
                
                
        
            

#Voice Author Views

class VoiceAuthorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/voice-authors/index.html'
    queryset = VoiceAuthor.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'voices'

class CreateVoiceAuthorView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'auth/voice-authors/create.html'
    model = VoiceAuthor
    form_class =  forms.VoiceAuthorForm
    success_url = '/voice-authors/'
    def form_valid(self, form):
        messages.success(self.request, 'Voice author created successfuly')
        return super().form_valid(form)
    
    
class UpdateVoiceAuthorView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'auth/voice-authors/update.html'
    model = VoiceAuthor
    form_class = forms.VoiceAuthorForm
    success_url = '/voice-authors/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Voice author updated successfuly')
        return super().form_valid(form) 
    
class DeleteVoiceAuthorView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'auth/voice-authors/delete.html'
    model = VoiceAuthor
    success_url = '/voice-authors/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Voice author deleted successfuly')
        return super().form_valid(form)     

class SubscriptionView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = "auth/subscriptions/index.html"
    queryset = Subcription.objects.all().order_by("-id")
    paginate_by = 10
    context_object_name = "subscriptions"
      


class CreateSubscriptionView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'auth/subscriptions/create.html'
    model = Subcription
    form_class = forms.SubscriptionForm
    success_url = "/subscriptions"
    
    def form_valid(self, form):
        messages.success(self.request, "Subscription was created successfully")
        return super().form_valid(form)
       
class UpdateSubscriptionView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'auth/subscriptions/update.html'
    model = Subcription
    form_class = forms.SubscriptionForm
    success_url = "/subscriptions"
    context_object_name = 'subscription'
    
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        return self.model.objects.get(uuid=uuid)
    
    def form_valid(self, form):
        messages.success(self.request, "Subscription was updated successfully")
        return super().form_valid(form) 
    
class DetailSubscriptionView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'auth/subscriptions/detail.html'
    model = Subcription     
    context_object_name = "subscription"
    
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        return self.model.objects.get(uuid=uuid)

class DeleteSubscriptionView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'auth/subscriptions/delete.html'
    model = Subcription
    success_url = "/subscriptions"
    template_object_name = 'subscription'
    
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        return self.model.objects.get(uuid=uuid)  
    def form_valid(self, form):
        messages.success(self.request, "Subscription was deleted successfully")
        return super().form_valid(form)                     

class PlanningView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/plannings/index.html'
    queryset = Planning.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'plannings'
    

#Todo
class CreatePlanningView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'auth/plannings/create.html'
    model = Planning
    form_class = forms.PlanningForm
    success_url = '/plannings/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Planning has been created successfuly')
        return super().form_valid(form)
    

class UpdatePlanningView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'auth/plannings/update.html'
    model = Planning
    form_class = forms.PlanningForm
    success_url = '/plannings/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Planning has been updated successfuly')
        return super().form_valid(form)
class DeletePlanningView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'auth/plannings/delete.html'
    model = Planning
    success_url = '/plannings/'
    context_object_name = 'plan'
    
    def form_valid(self, form):
        messages.success(self.request, 'Planning has been deleted successfuly')
        return super().form_valid(form)    
    
    
class AccountView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = "auth/accounts/index.html"
    queryset = Account.objects.all().order_by('-id')
    context_object_name = "accounts"
    paginate_by = 10

class CreateAccountView(LoginRequiredMixin, View):
    login_url = '/login/'
    template = 'auth/accounts/create.html'

    def get(self, request):
        form = forms.AccountForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.AccountForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfuly')
            return redirect(reverse('accounts'))
        return render(request, self.template, {'form': form})
class UpdateAccountView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = "auth/accounts/update.html"
    model = Account
    context_object_name = 'account'
    form_class = forms.AccountForm
    success_url = "/accounts"
    
    def form_valid(self, form):
        messages.success(self.request, 'Account has been updated successfuly')
        return super().form_valid(form)
    

class DeleteAccountView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = "auth/accounts/delete.html"
    model = Account
    context_object_name = 'account'
    success_url = "/accounts"
    
    def form_valid(self, form):
        messages.success(self.request, 'Account has been deleted successfuly')
        return super().form_valid(form)
    
class PromptView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/prompts/index.html'
    queryset = Prompt.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'prompts'
    
class DetailPromptView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'auth/prompts/detail.html'
    model = Prompt
    context_object_name = 'prompt'    

class CreatePromptView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'auth/prompts/create.html'
    model = Prompt
    form_class = forms.PromptForm
    success_url = '/prompts/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Your prompt has been created successfully')
        return super().form_valid(form)


class UpdatePromptView(LoginRequiredMixin, UpdateView):
    
    
    login_url = '/login/'
    template_name = 'auth/prompts/update.html'
    model = Prompt
    form_class = forms.PromptForm
    success_url = '/prompts/'
    context_object_name = 'prompt'
    
    def form_valid(self, form):
        messages.success(self.request, 'Prompt has been updated successfuly')
        return super().form_valid(form)
    
class DeletePromptView(LoginRequiredMixin, DeleteView):
    
    template_name = 'auth/prompts/delete.html'
    model = Prompt
    success_url = '/prompts/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Prompt has been Deleted successfuly')
        return super().form_valid(form)
    



class TitleView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/titles/index.html'
    queryset = Title.objects.all().order_by('-id')
    paginate_by = 10
    context_object_name = 'titles'
   
class DetailTitleView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'auth/titles/detail.html'
    model = Title
    context_object_name = 'title'

class CreateTitleView(LoginRequiredMixin, View):
    login_url = '/login/'
    template = 'auth/titles/create.html'

    def get(self, request):
        form = forms.TitleForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.TitleForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Title has been created successfuly')
            return redirect(reverse('titles'))
        return render(request, self.template, {'form': form})


class UpdateTitleView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = "auth/titles/update.html"
    model = Title
    context_object_name = 'title'
    form_class = forms.TitleForm
    success_url = "/titles/"
    
    def form_valid(self, form):
        messages.success(self.request, 'Title has been updated successfully')
        return super().form_valid(form)
class DeleteTitleView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = "auth/titles/delete.html"
    model = Title
    context_object_name = 'title'
    success_url = "/titles/"
    
    def form_valid(self, form):
        messages.success(self.request, 'Title has been deleted successfully')
        return super().form_valid(form)

class CharacterView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/characters/index.html'
    queryset = Character.objects.all().order_by('-id')
    context_object_name = 'characters'
    paginate_by = 10

class CreateCharacterView(LoginRequiredMixin, View):
    login_url = '/login/'
    template = 'auth/characters/create.html'

    def get(self, request):
        form = forms.CharacterForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.CharacterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Character has been created successfuly')
            return redirect(reverse('characters'))
        return render(request, self.template, {'form': form})


class UpdateCharacterView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'auth/characters/update.html'
    model = Character
    form_class = forms.CharacterForm
    success_url = '/characters'
    
    def form_valid(self, form):
        messages.success(self.request, 'Character has been updated successfuly')
        return super().form_valid(form)
    
    

class DeleteCharacterView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Character
    template_name = 'auth/characters/delete.html'
    context_object_name = 'character'
    success_url = ('/characters/')
    
    def form_valid(self, form):
        messages.success(self.request, 'Character has been deleted successfuly')
        return super().form_valid(form)
    

class PhraseView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = "auth/phrases/index.html"
    queryset = Phrase.objects.all().order_by("-id")
    paginate_by = 10
    context_object_name = "phrases"
    
class PhraseDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = "auth/phrases/detail.html"
    model = Phrase
    context_object_name = "phrase"
    

class CreatePhraseView(LoginRequiredMixin, View):
    login_url = '/login/'
    template = 'auth/phrases/create.html'

    def get(self, request):
        form = forms.PhraseForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.PhraseForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Phrase has been created successfuly')
            return redirect(reverse('phrases'))
        return render(request, self.template, {'form': form})


class UpdatePhraseView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = "auth/phrases/update.html"
    model = Phrase
    form_class = forms.PhraseForm
    context_object_name = 'phrase'
    
    success_url = '/phrases/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Phrase has been updated successfully')
        return super().form_valid(form)
class DeletePhraseView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = "auth/phrases/delete.html"
    model = Phrase
    context_object_name = 'phrase'
    
    success_url = '/phrases/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Phrase has been deleted successfully')
        return super().form_valid(form)
    

class BookView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'auth/books/index.html'
    queryset = Book.objects.all().order_by('-title')
    paginate_by = 5
    context_object_name = 'books'

class CreateBookView(LoginRequiredMixin, View):
    login_url = '/login/'
    template = 'auth/books/create.html'

    def get(self, request):
        form = forms.BookForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = forms.BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been created successfuly')
            return redirect(reverse('books'))
        return render(request, self.template, {'form': form})


class UpdateBookView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = "auth/books/update.html"
    model = Book
    form_class = forms.BookForm
    context_object_name = 'book'
    success_url = "/books"
    
    def form_valid(self, form):
        messages.success(self.request, 'Book has been updated successfully')
        
        return super().form_valid(form)
class DeleteBookView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = "auth/books/delete.html"
    model = Book
    context_object_name = "book"
    success_url = "/books"
    
    def form_valid(self, form):
        messages.success(self.request, 'Book has been deleted successfully')
        return super().form_valid(form)


class HookView(LoginRequiredMixin, ListView):
    template_name = 'auth/hooks/index.html'
    queryset = Hook.objects.all().order_by('-id')
    paginate_by = 5
    context_object_name = 'hooks'

class CreateHookView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'auth/hooks/create.html'
    form_class = forms.HookForm
    success_url = '/hooks'
    
    def form_valid(self, form):
        messages.success(self.request,"Hook has been created successfully")
        return super().form_valid(form)


class UpdateHookView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = "auth/hooks/update.html"
    model = Hook
    form_class = forms.HookForm
    context_object_name = 'hook'
    success_url = "/hooks"
    
    def form_valid(self, form):
        messages.success(self.request, 'Hook has been updated successfully')
        
        return super().form_valid(form)
class DeleteHookView(LoginRequiredMixin, DeleteView):
    template_name = "auth/hooks/delete.html"
    model = Hook
    context_object_name = "hook"
    success_url = "/hooks"
    
    def form_valid(self, form):
        messages.success(self.request, 'Hook has been deleted successfully')
        return super().form_valid(form)


