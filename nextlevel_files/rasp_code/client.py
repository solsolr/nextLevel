from socket import *
import threading
import time
import tkinter5 as tk
#import testgui as ts
import cv2
import pyautogui

a = []
# ctl = 2

def send(sock):
    while True:
        sendData = input('')
        sock.send(sendData.encode('utf-8'))
        if sendData == 'Q':
            clientSock.close()
            print('대화 종료')
            
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('')
        print('상대방>>', recvData.decode('utf-8'))
        a  = recvData.decode('utf-8').split() 
        print(a[1])       
        # if a[0] == "태풍":
        #     # pyautogui.write(["escape"])
        #     # tk.teapong()
        #     global ctl = 1
        # if a[0] == "일반":
        #     # pyautogui.typewrite('a', interval=1)
        #     # tk.nomal(9)
        #     # continue
        #     global ctl = 0
        
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('172.30.1.69', 9988))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
