import socket

PORT = 6000
HOST = socket.gethostbyname(socket.gethostname())
DESTINO = (HOST, PORT)
msg = ''

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Para finalizar a conexão click em Ctrl + x')
while msg != '\x18':
    msg = input("Digite sua mensagem: ")
    udp.sendto(msg.encode(), DESTINO)

upd.close()