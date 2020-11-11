import socket
import random

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

    inicio = 0
    result = ""

    while (inicio != tamanho):

        falha = random.randint(0,1)
        if(falha == 1):
            acerto = f"ACK {inicio}"
            _msg = udp.recv(1024)
            _msg = _msg.decode()
            
            udp.send(acerto.encode())

            result+= _msg
            inicio+=1

        else:
            erro = "ACK Lost"
            _msg = udp.recv(1024)
            udp.send(erro.encode())

    print(f"Mensagem recebida: {msg}")

udp.close()
