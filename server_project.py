import socket
import requests
import shutil
def download(params):
    try:
        param1 = params.get('param1')
        param2 = params.get('param2')
        param3 = params.get('param3')
        shutil.copy(param2,param3)
    except:
        return '0'
def upload(params):
    param1 = params.get('param1')
    param2 = params.get('param2')
    param3 = params.get('param3')   
    try:
        shutil.copy(param2,'c:/Users/USER/Desktop/HomeWork#5/files')
    except:
        return 0
socket_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port=12345
socket_server.bind((host,port))
socket_server.listen(1)
while (True):
    client_socket, client_address =  client_socket, client_address = socket_server.accept()
    params=client_socket.recv(1024).decode()
    if(params[0]=='2'):
        client_socket.send(download(params).encode())
    else:
        client_socket.send(upload(params).encode())
