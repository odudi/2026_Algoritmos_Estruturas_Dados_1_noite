carro01 ={"marca": "Doblo", "ano": 2006}
carro02 ={"marca": "Celta", "ano": 2008}
carro03 ={"marca": "Corsa", "ano": 2009}  

carro03["placa"] = "JDH-1G98"
#print(carro03)

frota = carro01, carro02
carro01["marca"] = "uno Mille"
print(frota)


def calcular(x, y):
    return x + y, x - y, x * y, x / y
result = calcular(5, 2)
print(result)

a, b, c, d = result
print(f"Soma: {a}, Subtração: {b}, Multiplicação: {c}, Divisão: {d}")


print("------------------------------------------------------------")
      
def printarNome(x):
    print("Nome:", x)

def printarValores (Valores):
    total = 0
    for n in Valores:
        total += n
    return total

numeros = ((1, 2), [1,2,3], [10, 20, 30, 40])
somas = map(printarValores, numeros)
print(list(somas))
nomes = "Alice", "Bob", "Charlie"

x = map(printarNome, nomes)
list(x)