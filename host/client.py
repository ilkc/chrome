from win10toast import ToastNotifier
import socket
import os

# 접속 정보 설정
SERVER_IP = '192.168.238.130'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# 클라이언트 소켓 설정




f = open("./intput.txt", "r")
line = f.readline()
line = line.replace('"', '')
f.close()
os.remove('intput.txt')
#client_msg = "https://www.mokpo.ac.kr/planweb/board/view.9is?pBoardId=BBSMSTR_000000000101&contentUid=4a94e3926d1a8834016d66a5f49a36ac&boardUid=4a94e3926f265c99016fd11bb7137b59&categoryUid1=0&nowPageNum=1&dataUid=4a94e3926cad5966016cadc4d5cd001c&nttId=848968"
client_msg = line

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # 서버에 접속
    client_socket.send(client_msg.encode())  # 서버에 메시지 전송
    msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
    msg = msg.decode('utf-8')
    toaster = ToastNotifier()
    if(int(msg) == 0):
        toaster.show_toast(client_msg,
                           "악성url입니다",
                           duration=10)
    if(int(msg) == 1):
        toaster.show_toast(client_msg,
                           "안전한 페이지 입니다",
                           duration=10)

    if(int(msg) >= 2 and int(msg) <= 5):
        toaster.show_toast(client_msg,
                           "악성 첨부파일 의심",
                           duration=10)

    if(int(msg) >= 6  and int(msg) <= 15):
        toaster.show_toast(client_msg,
                           "악성 첨부파일 주의",
                           duration=10)

    if(int(msg) >= 16  and int(msg) <= 30):
        toaster.show_toast(client_msg,
                           "악성 첨부파일 경고",
                           duration=10)

    if(int(msg) >= 31):
        toaster.show_toast(client_msg,
                           "악성 첨부파일 위험",
                           duration=10)

#    print("resp from server : {}".format(msg))  # 서버로부터 응답받은 메시지 출력