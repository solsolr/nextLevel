import socket
from _thread import *
import tkinter5 as tk
import pyautogui

HOST = '192.168.123.109'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)

        print("recive : ",repr(data.decode()))
        if data.decode() == "태풍":
            pyautogui.press('shift')
            tk.teapong()


start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')

while True:
    message = input('')
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())


client_socket.close()

