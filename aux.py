def codigo_binario(texto):
    sequencia_byte = bytearray(texto, "utf8")

    lista_byte = []

    for byte in sequencia_byte:
        binario = bin(byte)
        binario.replace("0b", "")
        lista_byte.append(binario)

    result=""
    for byte in lista_byte:
        result+= byte
    return result


def envio(conexao, inicio, msg):
    conexao.send(msg[inicio].encode())
    estado = conexao.recv(1024)
    estado = estado.decode()
    print(estado)

    return estado




def selecao_Seletiva(inicio, tamanho, janela, final, con, msg):
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