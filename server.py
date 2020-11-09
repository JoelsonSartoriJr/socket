import socket

HOST = ""
PORT = 6000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORT))

while True:
    msg, client = udp.recvfrom(1024)
    print(client, msg)
udp.close()
