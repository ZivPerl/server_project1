import socket
import json
host = '127.0.0.1'
port=12345
secceded=False
while(secceded==False):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host,port))
    path=input("enter path")
    number=input("2 for download 1 for upload")
    path_for_downloaded_file=input("path_for_downloaded_file")
    params={'param1':number, 'param2':path, 'param3':path_for_downloaded_file}
    params_str = json.dumps(params)
    client_socket.send(params_str.encode())
    recv=client_socket.recv(1024).decode()
    if(recv=="0"):
        print("eror try again")
    else:
        print("secceed")
        secceded=True
    client_socket.close()

