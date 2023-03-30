from django.contrib import admin
from .models import Area, User, Box, FileUpload, Traffic

admin.site.register(Area)
admin.site.register(User)
admin.site.register(Box)
admin.site.register(FileUpload)
admin.site.register(Traffic)
