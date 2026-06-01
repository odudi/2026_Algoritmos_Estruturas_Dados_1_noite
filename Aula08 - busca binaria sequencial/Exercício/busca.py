# Busca Binária
def busca_bin(v, n, k):
    inicio = 0
    fim = n - 1

    while inicio <= fim:
        centro = inicio + (fim - inicio) // 2

        if k == v[centro]:
            return centro
        elif k > v[centro]:
            inicio = centro + 1
        else:
            fim = centro - 1

    return -1


# Busca Sequencial
def busca_seq(v, n, k):
    for i in range(n):
        if v[i] == k:
            return i

    return -1


# Programa Principal
vetor_ordenado = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
vetor_desordenado = [23, 8, 91, 2, 56, 12, 38, 72, 5, 16]

valor = int(input("Digite o valor a ser procurado: "))

# Busca Binária
resultado_bin = busca_bin(vetor_ordenado, len(vetor_ordenado), valor)

if resultado_bin != -1:
    print(f"\n[Busca Binária] Valor encontrado na posição {resultado_bin}.")
else:
    print("\n[Busca Binária] Valor não encontrado.")

# Busca Sequencial
resultado_seq = busca_seq(vetor_desordenado, len(vetor_desordenado), valor)

if resultado_seq != -1:
    print(f"[Busca Sequencial] Valor encontrado na posição {resultado_seq}.")
else:
    print("[Busca Sequencial] Valor não encontrado.")