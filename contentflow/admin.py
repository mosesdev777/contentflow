from django.contrib import admin
from .models import Profile, Publication, SocialMedia, VoiceAuthor


admin.site.register(Profile)
admin.site.register(SocialMedia)
admin.site.register(VoiceAuthor)
admin.site.register(Publication)