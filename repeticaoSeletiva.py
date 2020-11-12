import random

def repeticao_seletiva_envio(inicio, janela, final, con, msg):
    cache = []
    flag = 0

    if(flag == 0):
        for i in range(janela):
            cache.append(inicio+i)
            print(f'Frame -> {inicio+i}')
    else:
        print(f'Frame -> {inicio}')

    con.send(str(inicio).encode())
    dado = con.recv(1024).decode()

    inicio = int(dado)
    
    if inicio not in cache:
        final = inicio + janela -1
        flag = 0
        for i in range(janela):
            cache.pop()

    else:
        flag = 1 

    print(f'ACK recebido do server {dado}')


def repeticao_seletiva_recebe(udp, tamanho, janela):
    inicio = int(udp.recv(1024).decode())
    
    lim = inicio + janela -1
    count = 0
    flag = 0
    ack = inicio
    novo = 1
    cache = []

    rand = random.randint(1, janela)

    if novo == 1:
        while(count != rand):
            temp = random.randint(inicio, lim)

            if temp not in cache:
                print(f'Frame recebido {temp}.')
                count += 1
                flag = 1
                cache.append(temp)
    else:
        print(f'Frame recebido {inicio}.')
        cache.append(inicio)
        flag = 1

    if flag == 1:
        for i in range(inicio, lim+1):
            if i not in cache:
                ack = i
                break
            ack = i + 1

    print(f'Enviando ACK -> {ack}')

    con.send(str(ack).encode())

    if ack > final:
        inicio = ack
        final = inicio + janela -1
        novo = 1
    else:
        novo = 0