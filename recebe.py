import socket
import random
from goBackN import go_Back_N_recebe

HOST = socket.gethostbyname(socket.gethostname())
PORT = 4321

udp = socket.socket()
udp.connect((HOST, PORT))
print('Conectado ...')


while True:
    msg = udp.recv(1024)
    msg = msg.decode()
    tamanho = udp.recv(1024)
    tamanho = int(tamanho.decode())

    go_Back_N_recebe(udp, tamanho)

    print(f"Mensagem recebida: {msg}")

udp.close()
