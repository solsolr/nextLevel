from django.contrib import admin

# Register your models here.
from .models import Area, FileUpload, Box, Traffic

# Area
class AreaAdmin(admin.ModelAdmin):
    search_fields = ['area_name']

admin.site.register(Area, AreaAdmin)


# FileUpload
class FileUploadAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(FileUpload, FileUploadAdmin)


# Box
class BoxAdmin(admin.ModelAdmin):
    search_fields = ['box_name']

admin.site.register(Box, BoxAdmin)


# Traffic
class TrafficAdmin(admin.ModelAdmin):
    search_fields = ['traffic_num']

admin.site.register(Traffic, TrafficAdmin)



