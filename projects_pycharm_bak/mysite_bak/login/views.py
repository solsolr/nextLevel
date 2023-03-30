from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Box, Traffic
from .forms import UserForm
from django.core.paginator import Paginator

from .tkinter5 import sinho, gin

import pandas as pd
import openpyxl
import folium

import json


def index(request):
    return render(request, 'login/index.html')


def auth(request):
    if request.method == 'POST' :
        page = request.POST.get('page', 1)
        input_id = request.POST.get('user_id')
        input_pwd = request.POST.get('user_pwd')
        try:
            user = User.objects.get(user_id=input_id, user_pwd=input_pwd)
        except User.DoesNotExist:
            user = None
        u = user
        box_list = u.area.box_set.all()
        paginator = Paginator(box_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'user': user, 'box_list' : page_obj}
        if user :
            return render(request, 'login/auth.html', context)

        return redirect('login:index')
    else :
        return redirect('login:index')


# def box_detail(request, user_id, box_id):
#     user = User.objects.get(user_id=user_id)
#     box = Box.objects.get(id=box_id)
#
#     # folium Map 위치 추출
#     loc = pd.read_excel("C:\projects\mysite\static\행정_법정동 중심좌표.xlsx", engine="openpyxl")
#     loc2 = loc[['시도', '시군구', '읍면동', '위도', '경도']]
#     for idx, row in loc2.iterrows():
#         addr = str(row['시도']) + " " + str(row['시군구']) + " " + str(row['읍면동'])
#         if box.box_area in addr:
#             m = folium.Map(
#                 location=[row['위도'], row['경도']],
#                 zoom_start=15
#             )
#
#     # folium Marker 경로 추출
#     out_list = []
#     in_list = []
#     data = pd.read_csv("C:\projects\mysite\static\신호등현황(개방표준).csv", encoding="cp949")
#     data2 = data[['소재지지번주소','위도','경도']]
#     for idx, row in data2.iterrows() :
#         if box.box_area in row['소재지지번주소'] :
#             in_list.append(row['위도'])
#             in_list.append(row['경도'])
#             in_list.append(row['소재지지번주소'])
#             out_list.append(in_list)
#             in_list = []
#
#     for i_li in out_list:
#         latitude = i_li[0]
#         longitude = i_li[1]
#         traffic_light_name = i_li[2]+'신호등'
#
#         try:
#             traffic = Traffic.objects.get(traffic_name=traffic_light_name)
#         except Traffic.DoesNotExist:
#             traffic = Traffic(box=box, traffic_name=traffic_light_name, traffic_text='넹넹', traffic_second=30,
#                         traffic_second2=30)
#             traffic.save()
#
#         f_m = folium.Marker([latitude, longitude],
#                       popup='<form action="">'
#                             '<input type="hidden" name="traffic_control" value="control">'
#                             '<input type="submit" value="제어">'
#                             '</form>',
#                       tooltip=traffic_light_name,
#                       icon=folium.Icon('red', icon='star'),
#                       )
#         f_m.add_to(m)
#
#     traffic_list = box.traffic_set.all()
#
#     context = {'user': user, 'box': box, 'traffic_list': traffic_list}
#
#     if request.GET.get('traffic_control')=='control':
#         page = request.GET.get('page', 1)
#         paginator = Paginator(traffic_list, 10)  # 페이지당 10개씩 보여주기
#         page_obj = paginator.get_page(page)
#         context = {'box': box, 'traffic_list': page_obj, 'user': user}
#         return render(request, 'login/box_detail.html', context)
#
#     m.save(r'C:\projects\mysite\templates\login\map.html')
#
#     return render(request, 'login/map.html', context)

def box_detail(request, user_id, box_id):
    user = User.objects.get(user_id=user_id)
    box = Box.objects.get(id=box_id)
    latitude = ''
    longitude = ''


    # kakao Map 위치 추출
    loc = pd.read_excel("C:\projects\mysite\static\행정_법정동 중심좌표.xlsx", engine="openpyxl")
    loc2 = loc[['시도', '시군구', '읍면동', '위도', '경도']]
    for idx, row in loc2.iterrows():
        addr = str(row['시도']) + " " + str(row['시군구']) + " " + str(row['읍면동'])
        if box.box_area in addr:
            latitude = row['위도']
            longitude = row['경도']
    map_loc_out_list = []
    map_loc_out_list.append(latitude)
    map_loc_out_list.append(longitude)


    # kakao Marker 경로 추출
    out_list = []
    in_list = []
    data = pd.read_csv("C:\projects\mysite\static\신호등현황(개방표준).csv", encoding="cp949")
    data2 = data[['소재지지번주소','위도','경도']]
    for idx, row in data2.iterrows() :
        if box.box_area in row['소재지지번주소'] :
            in_list.append(row['위도'])
            in_list.append(row['경도'])
            traffic_light_name = row['소재지지번주소']+' 신호등'
            in_list.append(traffic_light_name)
            out_list.append(in_list)
            in_list = []
            try:
                traffic = Traffic.objects.get(traffic_name=traffic_light_name)
            except Traffic.DoesNotExist:
                traffic = Traffic(box=box, traffic_name=traffic_light_name, traffic_text='넹넹', traffic_second=30,
                            traffic_second2=30)
                traffic.save()

    marker_loc_out_list = out_list

    traffic_list = box.traffic_set.all()

    traffic_id_list = []
    for t in traffic_list:
        traffic_id_list.append(t.id)


    trafficdict = {
                    'user_id': user.user_id,
                    'box_id': box.id,
                    'traffic_id_list': traffic_id_list,
                    'map_loc_out_list': map_loc_out_list,
                    'marker_loc_out_list': marker_loc_out_list
    }

    trafficJson = json.dumps(trafficdict)

    # context = {'user': user, 'box': box, 'traffic_list': traffic_list, 'map_loc_out_list': map_loc_out_list,
    #            'marker_loc_out_list': marker_loc_out_list}

    context = {'trafficJson': trafficJson}

    return render(request, 'login/kakao_map_test.html', context)

def traffic_detail(request, user_id, box_id, traffic_id):
    user = User.objects.get(user_id=user_id)
    box = Box.objects.get(id=box_id)
    traffic = Traffic.objects.get(id=traffic_id)
    context = {'traffic': traffic, 'box': box, 'user': user}
    return render(request, 'login/traffic_detail.html', context)



def traffic(request):
    sinho("ㅇㅇ", 20)
    user_id = request.POST.get('user_id')
    box_id = request.POST.get('box_id')
    traffic_id = request.POST.get('traffic_id')
    traffic_message = request.POST.get('traffic_message')

    return traffic_detail(request, user_id, box_id, traffic_id)


def traffic2(request):
    gin()
    user_id = request.POST.get('user_id')
    box_id = request.POST.get('box_id')
    traffic_id = request.POST.get('traffic_id')
    return traffic_detail(request, user_id, box_id, traffic_id)

# def kakao(request):
#     return render(request, 'login/kakao_map_test.html')