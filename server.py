from socket import *
import pyautogui
import threading


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8080))

print('클라이언트 접속 대기중...')
serverSocket.listen(1)

connectionSock, addr = serverSocket.accept()
print(str(addr), '에서 접속이 확인되었습니다.')

# readable = [connectionSock]


def thread_target():
    while True:
        data = connectionSock.recv(1024)

        if not data:
            pass
        else:
            # print('받은 데이터: ', data.decode('utf-8'))
            split_data = data.decode('utf-8').split('_')

            if data.decode('utf-8') == 'REQUEST_CONNECT':
                connectionSock.send('OK'.encode('utf-8'))
                print('메세지 전송 완료')

            if data.decode('utf-8') == 'KEYBOARD_UP':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('up')
            elif data.decode('utf-8') == 'KEYBOARD_DOWN':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('down')
            elif data.decode('utf-8') == 'KEYBOARD_LEFT':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('left')
            elif data.decode('utf-8') == 'KEYBOARD_RIGHT':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('right')
            elif data.decode('utf-8') == 'KEYBOARD_SPACE':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('space')
            elif data.decode('utf-8') == 'KEYBOARD_ENTER':
                connectionSock.send('OK'.encode('utf-8'))
                pyautogui.press('enter')

            elif split_data[0] == 'MOUSEMOVE':
                print(split_data[1])
                print(split_data[2])

                pyautogui.moveRel(float(split_data[1]) * 2, float(split_data[2]) * 2)

                split_data = None


thread_control = threading.Thread(target=thread_target)
# thread_control.daemon = True
thread_control.start()
