valor = int(input("Ingresa un número: "))

def factorialFor(valor):
    total = 1
    lista = []
    for veces in range(1, valor + 1):
        total = veces * total
        lista.append(veces)
    lista = lista[::-1]
    print(valor,"! = ", str(lista).replace(",", " x"), " = ", total, sep = "")

def factorialWhile(valor):
    total = 1
    lista = []
    valor2 = valor
    while valor > 0:
        total = valor * total
        lista.append(valor)
        valor -= 1
    print(valor2, "! = ", str(lista).replace(",", " x"), " = ", total, sep = "")

#factorialFor(valor)
factorialWhile(valor)