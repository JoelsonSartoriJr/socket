import socket
from aux import codigoBinario
from goBackN import go_Back_N

PORT = 4321
HOST = socket.gethostname()

udp = socket.socket()
udp.bind((HOST, PORT))

udp.listen(1)
print('Esperando conexão ....')
con, _ = udp.accept()
print("Connectado")

while True:
    msg = input(str("Digite sua mensagem: "))
    con.send(msg.encode())

    if msg == "exit":
        break

    msg = codigoBinario(msg)
    tamanho = len(msg)
    con.send(str(tamanho).encode())

    inicio = 0
    janela = int(input('Digite o número da janela: ')) -1
    final = janela

    go_Back_N(inicio, tamanho, janela, final, con, msg)

udp.close()
