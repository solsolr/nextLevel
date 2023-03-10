from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input('')
        sock.send(sendData.encode('utf-8'))
        
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방>>', recvData.decode('utf-8'))
        # 추가한 부분 client 종료시 무한 루프 탈출
        if not recvData:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
        
port = 9988

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('172.30.1.6', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
