from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField


from .models import (Profile, Publication, SocialMedia,
                     VoiceAuthor, Channel, Subcription,
                     Planning, Account, Prompt, Title,
                     Character, Phrase, Book, Hook, Contact
                     )

class PublicationForm(ModelForm):
    social_media = forms.ModelMultipleChoiceField(
        queryset=SocialMedia.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})

    )
    class Meta:
        model = Publication
        fields = '__all__'
        exclude = ('user', 'uuid', 'slug' )
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 5}),
            'script': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 5}),
            'thumbnail_title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'voice_type': forms.Select(attrs={'class': 'form-select my-2'}),
            'voice_author': forms.Select(attrs={'class': 'form-select my-2'}),
            'voice_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'status': forms.Select(attrs={'class': 'form-select my-2'}),
            'content_format': forms.Select(attrs={'class': 'form-select my-2'}),
            'background_music': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'voice_author': forms.Select(attrs={'class': 'form-select my-2'}),
            'social_media': forms.CheckboxSelectMultiple(attrs={'class': ''}),
            'channel': forms.Select(attrs={'class': 'form-select my-2'})
            
            
        }
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model =  Profile
        fields = ('avatar', )
        
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'my-2 form-control'}),
        }

class UserChangeForm( forms.ModelForm ):
    
    class Meta:
        fields = '__all__'
        exclude =('username', 'password', 'is_superuser',
                  'is_staff', 'is_active', 'groups', 'user_permissions',
                  'date_joined', 'last_login', )
        
        model = User    
        
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'my-2 form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'my-2 form-control'}),
            'email': forms.TextInput(attrs={'class': 'my-2 form-control'}),
        }    
class LoginForm(forms.Form):
    username =  forms.CharField(max_length=20, widget=forms.TextInput( attrs={
        'class': 'form-control my-2'
    }))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control my-2'
    }))
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control my-2'
    }))
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class':'form-control my-2'
    }))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class':'form-control my-2'
    }))
    
    
    def clean_username(self):
        username:str = self.cleaned_data.get('username')
        lower_username = username.lower()
        
        return lower_username
    

class ChannelForm(forms.ModelForm):
    social_media = forms.ModelMultipleChoiceField(
        queryset=SocialMedia.objects.all(),
        widget=forms.SelectMultiple(attrs={'class':'form-control my-2'}))
    
    class Meta:
        model = Channel    
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }    
        
class VoiceAuthorForm(forms.ModelForm):
    class Meta:
        model = VoiceAuthor    
        fields = '__all__' 
        
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'})
        }       
        
class SocialMediaForm(forms.ModelForm):
    
    class Meta:
        model = SocialMedia 
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'icon':forms.FileInput(attrs={'class': 'form-control'}),
        }            

class VoiceAuthorForm(forms.ModelForm):
    
    class Meta:
        model = VoiceAuthor
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }    
        
class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subcription
        fields = '__all__'
        exclude = ('uuid',)
        
        widgets = {
            'platform': forms.TextInput(attrs={'class':'form-control my-2'}),
            'plan': forms.TextInput(attrs={'class':'form-control my-2'}),
            'amount': forms.NumberInput(attrs={'class':'form-control my-2'}),
            'mail': forms.EmailInput(attrs={'class':'form-control my-2'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'AAAA-MM-DD', 'type':'date'}),
            'renewal': forms.Select(attrs={'class':'form-select my-2'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input my-2'}),
        }            
        
class PlanningForm(forms.ModelForm):
    
    class Meta:
        model = Planning
        fields = '__all__'
        
        widgets = {
            'social_network':forms.Select(attrs={'class':'form-control my-2'}),
            'channel':forms.Select(attrs={'class':'form-control my-2'}),
            'frecuency':forms.Select(attrs={'class':'form-control my-2'}),
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

        widgets = {
            "platform":forms.TextInput(attrs={'class':'form-control my-3'}),
            "email":forms.TextInput(attrs={'class':'form-control my-3'}),
            "purpose":forms.TextInput(attrs={'class':'form-control my-3'}),
            "username":forms.TextInput(attrs={'class':'form-control my-3'}),
            "phone":forms.TextInput(attrs={'class':'form-control my-3'}),
            "two_factor_authenticator":forms.Select(attrs={'class':'form-select my-3'}),         
            
        }


class PromptForm(forms.ModelForm):
    
    class Meta:
        model = Prompt
        fields = '__all__'

        widgets = {
            'channel': forms.Select(attrs={'class':'form-select my-2'}),
            'content_format': forms.Select(attrs={'class':'form-select my-2'}),
            'text': RichTextFormField()#CKEditorWidget()#SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}) #forms.Textarea(attrs={'class':'form-select my-2', 'placeholder':'Please enter your prompt here'}),
        }
        
        

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'

        widgets = {
            "name":forms.TextInput(attrs={'class':'my-2 form-control'}),
            "channel":forms.Select(attrs={'class':'my-2 form-select'}),
            "publish_date":forms.DateInput(attrs={'class':'my-2 form-control', 'type':'date'}),
            "content_format":forms.Select(attrs={'class':'my-2 form-select'}),
            "status": forms.CheckboxInput(attrs={'class':'my-2 form-check-input'})
        }
class CharacterForm(forms.ModelForm):
    
    class Meta:
        model = Character
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'type': forms.Select(attrs={'class': 'form-select my-2'}),
        }


class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = '__all__'

        widgets = {
            'date_used': forms.DateInput(attrs={'type': 'date', 'class':'my-2 form-control'}),
            'channel': forms.Select(attrs={'class': 'my-2 form-select'}),
            'author': forms.TextInput(attrs={'class':'my-2 form-control'}),
            'text': forms.Textarea(attrs={'class':'my-2 form-control'}),
            'is_used': forms.CheckboxInput(attrs={'class':'my-2 form-check-input'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control my-2'}),
            "author": forms.TextInput(attrs={'class': 'form-control my-2'}),
            "purpose": forms.Select(attrs={'class': 'form-select my-2'}),
            
        }

class HookForm(forms.ModelForm):
    class Meta:
        model = Hook
        fields = '__all__'
        exclude = ('uuid',)

        widgets = {
            "hook":forms.Textarea(attrs={"class":"form-control"})
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'message')

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control my-2 shadow'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control my-2 shadow'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control my-2 shadow'
            }),
        }
