import socket
from aux import codigoBinario

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

    while (inicio != tamanho):

        while(inicio!=(tamanho-janela)):

            con.send(msg[inicio].encode())
            retorno = con.recv(1024)
            retorno = retorno.decode()
            print(retorno)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1 
                final +=1

            else:
                print('Dados perdidos')

        while (inicio != tamanho):

            con.send(msg[inicio].encode())
            retorno = con.recv(1024)
            retorno = retorno.decode()
            print(retorno)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1 
                final +=1

            else:
                print('Dados perdidos')

upd.close()
