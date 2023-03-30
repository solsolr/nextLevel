from django.forms import ModelForm
from .models import FileUpload, Traffic


class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile', 'content']


class TrafficForm(ModelForm):
    class Meta:
        model = Traffic
        fields = ['traffic_name', 'traffic_text', 'traffic_second', 'traffic_second2']

