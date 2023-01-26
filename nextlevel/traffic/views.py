from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm, TrafficForm
from .models import FileUpload, Box, Traffic
from common.models import User

# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed  # 삭제


def index(request):
    return HttpResponse("안녕하세요 traffic에 오신것을 환영합니다.")

def fileUpload(request):
    images_list = FileUpload.objects.order_by('id')
    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES["imgfile"]
            fileupload = FileUpload(
                title=title,
                content=content,
                imgfile=img,
            )
            fileupload.save()
            return redirect('traffic:fileupload')
    else:
        form = FileUploadForm
    context = {
        'images_list': images_list,
        'fileuploadForm': form,
    }
    return render(request, 'traffic/fileupload.html', context)

def detail(request, box_id):
    box = get_object_or_404(Box, pk=box_id)
    context = {'box': box}
    return render(request, 'traffic/box_detail.html', context)

def traffic_create(request, box_id):
    box = get_object_or_404(Box, pk=box_id)
    if request.method == "POST":
        form = TrafficForm(request.POST)
        if form.is_valid():
            traffic = form.save(commit=False)
            try:
                img = request.FILES["img1"]
                img2 = request.FILES["img2"]
            except:
                img = None
                img2 = None

            traffic.traffic_image = img
            traffic.traffic_image2 = img2
            traffic.box = box
            traffic.save()
            return redirect('traffic:detail', box_id=box.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'box': box, 'form': form}
    return render(request, 'traffic/box_detail.html', context)