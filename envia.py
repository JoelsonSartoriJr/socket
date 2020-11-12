import socket
from aux import codigo_binario
from goBackN import go_Back_N_envio
from repeticaoSeletiva import repeticao_seletiva_envio

PORT = 4321
HOST = socket.gethostname()

udp = socket.socket()
udp.bind((HOST, PORT))

udp.listen(1)
print('Esperando conexão ....')
con, _ = udp.accept()
print('Connectado.....')
print('Para finalizar a conexão digite exit.')
while True:
    print('-'*50)
    msg = input('Digite sua mensagem:' )
    con.send(msg.encode())
    if msg == 'exit':
        udp.close()
        break

    algoritmo = input('Digite 1 para usar o algoritmo GBN, 2 para o algoritmo Repetição seletiva: ')
    con.send(algoritmo.encode())

    msg = codigo_binario(msg)
    tamanho = len(msg)
    con.send(str(tamanho).encode())

    janela = int(input('Digite o número da janela: ')) -1

    algoritmo = int(algoritmo)
    if algoritmo == 1:
        go_Back_N_envio(tamanho, janela, con, msg)
    elif algoritmo == 2:
        repeticao_seletiva_envio(tamanho, janela, con, msg)
    else:
        print('Opção invalida !! :(')