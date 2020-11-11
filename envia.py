import socket
from aux import codigo_binario
from goBackN import go_Back_N_envio

PORT = 4321
HOST = socket.gethostname()

udp = socket.socket()
udp.bind((HOST, PORT))

udp.listen(1)
print('Esperando conexão ....')
con, _ = udp.accept()
print("Connectado")
while True:
    print("Para finalizar a conexão digite exit.")
    msg = input(str("Digite sua mensagem: "))
    con.send(msg.encode())

    if msg == "exit":
        udp.close()
        break

    msg = codigo_binario(msg)
    tamanho = len(msg)
    con.send(str(tamanho).encode())

    inicio = 0
    janela = int(input('Digite o número da janela: ')) -1
    final = janela

    go_Back_N_envio(inicio, tamanho, janela, final, con, msg)

