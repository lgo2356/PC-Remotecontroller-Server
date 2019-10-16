from socket import *


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('연결 완료')
clientSock.send('나는 클라이언트입니다.'.encode('utf-8'))

print('메세지 전송 완료')

data = clientSock.recv(1024)
print('받은 데이터: ', data.decode('utf-8'))

while True:
    print('대기중...')
