from aux import envio
import random

def go_Back_N_envio(inicio, tamanho, janela, final, con, msg):
    while (inicio != tamanho):
    
        while(inicio!=(tamanho-janela)):

            retorno = envio(con, inicio, msg)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1
                final +=1

            else:
                print('Dados perdidos')

        while (inicio != tamanho):

            retorno = envio(con, inicio, msg)
            if(retorno != "ACK Lost"):
                print(f'Recebido! Janela no range {inicio+1} até {final+1}. Enviando novos pacotes.')
                inicio +=1 
                final +=1

            else:
                print('Dados perdidos')

def go_Back_N_recebe(udp, inicio, tamanho):
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