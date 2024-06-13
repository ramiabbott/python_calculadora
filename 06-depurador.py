def saludos(texto):
    resultado = 0
    for _ in texto:
        resultado +=1
    return resultado

l = saludos("Hola ramiro")
print(l)