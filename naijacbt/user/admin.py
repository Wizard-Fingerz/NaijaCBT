from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('department', 'location', 'birth_date')


admin.site.register(Profile, ProfileAdmin)