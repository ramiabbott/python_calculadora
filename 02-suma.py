def suma(*numeros):
    resultado=0
    for numero in numeros:
        resultado += int(numero)
    print(resultado)



suma(5, 10, 15) 
suma("1", "3", "78")
suma(15, 15, 15, 15, 15, 95)