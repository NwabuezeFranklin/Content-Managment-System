from django.contrib import admin

# Register your models here.
from .models import Profile, Image, Comment

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
