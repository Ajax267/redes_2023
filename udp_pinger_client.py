import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_port = 12000
client_socket.connect(('', server_port))
client_socket.settimeout(1)
message = 'PING'
nPings = 0
rtt = 0
while (nPings < 10):
    nPings = nPings + 1
    client_socket.send(message.encode())
    tempo = time.time()
    try:
        response = client_socket.recv(1024).decode()
        if response == message:
            rtt = (time.time() - tempo) * 1000
            print(response + ' ' + str(nPings) + ' ' + str(rtt))
    except socket.error:
        print("Request timed out")
        