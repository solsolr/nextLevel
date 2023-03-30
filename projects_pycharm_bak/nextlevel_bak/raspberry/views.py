from django.shortcuts import render
from django.http import HttpResponse
import socket
from _thread import *

# Create your views here.
def index(request):
    return HttpResponse("hello raspberryPI")


def mqttTest(request):
    return render(request, 'raspberry/mqtt.html')

def mqttpir(request):
    return render(request, 'raspberry/mqtt_pir.html')

def mqttsinho(request):
    return render(request, 'raspberry/mqtt_sinho.html')

def socketTest(request):
    return render(request, 'raspberry/socket.html')


def clientSocket(request):
    message = request.POST.get('message')
    HOST = '172.30.1.80'
    PORT = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # 서버로부터 메세지를 받는 메소드
    # 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
    # def recv_data(client_socket):
    #     while True:
    #         data = client_socket.recv(1024)
    #
    #         print("recive : ", repr(data.decode()))
    #
    # start_new_thread(recv_data, (client_socket,))
    print('>> Connect Server')
    print('>>message' + message)
    if request.method == "POST":
        client_socket.send(message.encode())
        client_socket.close()
        return redirect('rasp:socket')
    else:
        context = {'message': message}
        return render(request, 'raspberry/socket.html', context)


# 서버 소켓 사용할때 쓰는 코드
from django.http import HttpResponse
from django.shortcuts import render, redirect
import socket
from _thread import *
value = 0

# Create your views here.
def rasp(request):
    # 서버 IP 및 열어줄 포트
    HOST = '172.30.1.93'
    PORT = 9999
    # 서버 소켓 생성
    print('>> Server Start')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    try:
        print('>> Wait')
        client_socket, addr = server_socket.accept()
        start_new_thread(threaded, (client_socket, addr))
    except Exception as e:
        print('에러는? : ', e)
    finally:
        server_socket.close()
        return render(request, 'html/rasp.html', {
                'coms' : 'hihi',
            })

def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])
    cnt = 1
    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:
        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            print('>> Received from ' + addr[0], ':', addr[1], data.decode())
            cnt += 1
            if cnt >= 60:
                client_socket.close()
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
    client_socket.close()