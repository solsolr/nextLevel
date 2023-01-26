from django.shortcuts import render, redirect
from .models import User
from .form import UserForm
from traffic.models import Area

# Create your views here.
def index(request):
    return render(request, 'common/index.html')

def login(request):
    if request.method == 'POST':
        input_id = request.POST.get('user_id')
        input_pwd = request.POST.get('user_pwd')
        try:
            user = User.objects.get(user_id=input_id, user_pwd=input_pwd)
        except User.DoesNotExist:
            user = None
        a = user.area
        box_list = a.box_set.all()
        context = {'user': user, 'box_list': box_list}
        if user:
            return render(request, 'traffic/box_list.html', context)
            # return render(request, 'traffic/index.html', context)
    else:
        return redirect('common:index')
    return redirect('common:index')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # input_area = request.POST.get('area')
        # area = Area(area_name=input_area)
        pwd = request.POST.get('user_pwd')
        pwd2 = request.POST.get('user_pwd2')
        if form.is_valid() and (pwd==pwd2):
            user = form.save(commit=False)
            # user.area = area
            user.save()
            return redirect('common:index')
    else :
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/sign_up.html', context)