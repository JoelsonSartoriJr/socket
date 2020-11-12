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


def envio(con, inicio, msg):
    con.send(msg[inicio].encode())
    estado = con.recv(1024)
    estado = estado.decode()
    print(estado)

    return estado