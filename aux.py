def codigoBinario(texto):
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