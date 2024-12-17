from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    #publications
    path('publications', views.PublicationListView.as_view(), name='publications'),
    path('publications/datails/<uuid>', views.PublicationDetailView.as_view(), name='publication-details'),
    path('publications/create', views.PublicationCreateView.as_view(), name='create-publication'),
    path('publications/update/<uuid>', views.UpdatePublicationView.as_view(), name='update-publication'),
    path('publications/delete/<uuid>', views.DeletePublication.as_view(), name='delete-publication'),
    
    #profile
    path('profile-datails/<int:pk>/', views.UserProfileView.as_view(), name='profile-datails'),
    path('profile-change/<int:pk>/', views.UserProfileChangeView.as_view(), name='profile-change'),
    path('profile-delete/<int:pk>/', views.UserProfileDeleteView.as_view(), name='profile-delete'),
    path('account-deleted/', views.UserProfileChangeView.as_view(), name='profile-deleted'),
    

    
    #channels
    path('channels', views.ChannelListView.as_view(), name='channels'),
    path('channels/delete/<int:pk>', views.DeleteChannelView.as_view(), name='delete-channel'),
    path('channels/create', views.CreateChannelView.as_view(), name='create-channel'),
    path('channels/update/<int:pk>', views.UpateChannelView.as_view(), name='update-channel'),
    
    #social medias
    path('social-medias/', views.SocialMediaView.as_view(), name='social-medias'),
    path('social-medias/create/', views.CreateSocialMediaView.as_view(), name='create-social-media'),
    path('social-medias/update/<int:pk>/', views.UpdateSocialMediaView.as_view(), name='update-social-media'),
    path('social-medias/delete/<int:pk>/', views.DeleteSocialMediaView.as_view(), name='delete-social-media'),
    
    #Voice Author
    path('voice-authors/', views.VoiceAuthorView.as_view(), name='voice-authors'),
    path('voice-authors/create/', views.CreateVoiceAuthorView.as_view(), name='create-voice-authors'),
    path('voice-authors/update/<int:pk>/', views.UpdateVoiceAuthorView.as_view(), name='update-voice-authors'),
    path('voice-authors/delete/<int:pk>/', views.DeleteVoiceAuthorView.as_view(), name='delete-voice-authors'),

    #Subscriptions
    path('subscriptions', views.SubscriptionView.as_view(), name='subscriptions'),
    path('subscriptions/detail/<uuid:uuid>', views.DetailSubscriptionView.as_view(), name='detail-subscription'),
    path('subscriptions/create', views.CreateSubscriptionView.as_view(), name='create-subscription'),
    path('subscriptions/update/<uuid:uuid>', views.UpdateSubscriptionView.as_view(), name='update-subscription'),
    path('subscriptions/delete/<uuid:uuid>', views.DeleteSubscriptionView.as_view(), name='delete-subscription'),
    
    #Plannings 
    path('plannings/', views.PlanningView.as_view(), name='plannings'),
    path('plannings/create/', views.CreatePlanningView.as_view(), name='create-planning'),
    path('plannings/update/<int:pk>/', views.UpdatePlanningView.as_view(), name='update-planning'),
    path('plannings/delete/<int:pk>/', views.DeletePlanningView.as_view(), name='delete-planning'),

    #Accounts
    path('accounts', views.AccountView.as_view(), name='accounts'),
    path('accounts/create/', views.CreateAccountView.as_view(), name='create-account'),
    path('accounts/update/<int:pk>/', views.UpdateAccountView.as_view(), name='update-account'),
    path('accounts/delete/<int:pk>/', views.DeleteAccountView.as_view(), name='delete-account'),

    #Prompts
    path('prompts/', views.PromptView.as_view(), name='prompts'),
    path('prompts/create/', views.CreatePromptView.as_view(), name='create-prompt'),
    path('prompts/details/<int:pk>/', views.DetailPromptView.as_view(), name='detail-prompt'),
    path('prompts/update/<int:pk>/', views.UpdatePromptView.as_view(), name='update-prompt'),
    path('prompts/delete/<int:pk>/', views.DeletePromptView.as_view(), name='delete-prompt'),

    #Title
    path('titles/', views.TitleView.as_view(), name='titles'),
    path('titles/details/<int:pk>/', views.DetailTitleView.as_view(), name='title-detail'),
    path('titles/create/', views.CreateTitleView.as_view(), name='create-title'),
    path('titles/update/<int:pk>/', views.UpdateTitleView.as_view(), name='update-title'),
    path('titles/delete/<int:pk>/', views.DeleteTitleView.as_view(), name='delete-title'),

    #Characters
    path('characters/', views.CharacterView.as_view(), name='characters'),
    path('characters/create', views.CreateCharacterView.as_view(), name='create-character'),
    path('characters/update/<int:pk>', views.UpdateCharacterView.as_view(), name='update-character'),
    path('characters/delete/<int:pk>', views.DeleteCharacterView.as_view(), name='delete-character'),

    # Phrases
    path('phrases/', views.PhraseView.as_view(), name='phrases'),
    path('phrases/datails/<int:pk>', views.PhraseDetailView.as_view(), name='details-phrase'),
    path('phrases/create/', views.CreatePhraseView.as_view(), name='create-phrase'),
    path('phrases/update/<int:pk>/', views.UpdatePhraseView.as_view(), name='update-phrase'),
    path('phrases/delete/<int:pk>/', views.DeletePhraseView.as_view(), name='delete-phrase'),
    
    # Books
    path('books', views.BookView.as_view(), name='books'),
    path('books/create', views.CreateBookView.as_view(), name='create-book'),
    path('books/update/<int:pk>', views.UpdateBookView.as_view(), name='update-book'),
    path('books/delete/<int:pk>', views.DeleteBookView.as_view(), name='delete-book'),
    
    # Hooks
    path('hooks', views.HookView.as_view(), name='hooks'),
    path('hooks/create', views.CreateHookView.as_view(), name='create-hook'),
    path('hooks/update/<int:pk>', views.UpdateHookView.as_view(), name='update-hook'),
    path('hooks/delete/<int:pk>', views.DeleteHookView.as_view(), name='delete-hook'),


]

