## SERVER ##
import socket
import threading

## Server IP and Port ##

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3000
print('>> Server Start with ip :', HOST)

########## processing in thread ##
## new client, new thread ##

def listen(client_socket, addr):
    ## process until client disconnect ##
    while True:
        try:
            ## send client if data recieved(echo) ##
            data = client_socket.recv(1024)

            if not data:
                continue
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())

            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            client_socket.send(data)
        
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
    
    # if client_socket in client_sockets:
    #     client_sockets.remove(client_socket)
    #     print('remove client list : ', len(client_sockets))
    client_socket.close()


########## processing in thread ##
## send message to client ##

def send(client_socket, addr):
    while True:
        try:
            data = input()
            if not data:
                print('>> ')
                break
            
            print('>> send to ' + addr[0], ':', addr[1], data)

            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            client_socket.send(data.encode())
        
        except ConnectionResetError as e:
            break
    client_socket.close()

############# Create Socket and Bind ##

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

############# Client Socket Accept ##
print('>> Wait...')
client_socket, addr = server_socket.accept()
print('>> Connected by :', addr[0], ':', addr[1])

try:
    # while True:
        # client_sockets.append(client_socket)
    # start_new_thread(listen, (client_socket, addr))
    # start_new_thread(send, (client_socket, addr))
    # print("참가자 수 : ", len(client_sockets))
    # 스레드 생성
    listen_thread = threading.Thread(target=listen, args=(client_socket, addr))
    send_thread = threading.Thread(target=send, args=(client_socket, addr))

    # 스레드 시작
    listen_thread.start()
    send_thread.start()

    # 스레드가 종료될 때까지 기다림
    listen_thread.join()
    send_thread.join()
except Exception as e:
    print('에러 : ', e)

finally:
    print('>> End')
    server_socket.close()