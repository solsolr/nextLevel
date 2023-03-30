from django.contrib import admin
from .models import User
# Register your models here.
#User
class UserAdmin(admin.ModelAdmin):
    search_fields = ['user_name']

admin.site.register(User, UserAdmin)