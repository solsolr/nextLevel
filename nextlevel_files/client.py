from socket import *
import threading
import time


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
        print('상대방>> ', recvData.decode('utf-8'))
        
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
