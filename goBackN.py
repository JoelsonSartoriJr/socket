from aux import envio

def go_Back_N(inicio, tamanho, janela, final, con, msg):
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