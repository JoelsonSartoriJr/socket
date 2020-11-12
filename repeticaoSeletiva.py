from aux import envio
import random

def repeticao_seletiva_envio(tamanho, janela, con, msg):
    inicio = 0
    final = janela
    cache = []
    while (inicio != tamanho):
    
        while(inicio!=(tamanho-janela)):

            retorno = envio(con, inicio, msg)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1
                final +=1

            else:
                cache.append(inicio)
                inicio +=1
                final +=1
                
        print(cache)
        while len(cache) != 0:
            for i in cache:
                retorno = envio(con, int(i), msg)

                if(retorno != "ACK Lost"):
                    print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                    cache.pop(0)
                else:
                    print('Dados perdidos')

        while (inicio != tamanho):

            retorno = envio(con, inicio, msg)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1 
                final +=1

            else:
                cache.append(inicio)
                inicio +=1
                final +=1

def repeticao_seletiva_recebe(udp, tamanho):
    result = ""
    inicio = 0
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