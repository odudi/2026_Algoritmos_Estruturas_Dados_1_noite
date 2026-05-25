from Arvore import Arvore


a = Arvore()

# inserções
a.raiz = a.inserir(a.raiz, 48)
a.raiz = a.inserir(a.raiz, 22)
a.raiz = a.inserir(a.raiz, 17)
a.raiz = a.inserir(a.raiz, 13)
a.raiz = a.inserir(a.raiz, 64)
a.raiz = a.inserir(a.raiz, 75)
a.raiz = a.inserir(a.raiz, 52)
a.raiz = a.inserir(a.raiz, 31)
a.raiz = a.inserir(a.raiz, 19)
a.raiz = a.inserir(a.raiz, 100)



# Em Ordem
print("\n--- Em Ordem (ERD) ---")
a.imprimirEmOrdem(a.raiz)

# Pré Ordem
print("\n\n--- Pré Ordem (RED) ---")
a.imprimirPreOrdem(a.raiz)

# Pós Ordem
print("\n\n--- Pós Ordem (EDR) ---")
a.imprimirPosOrdem(a.raiz)

# Reverso
print("\n\n--- Ordem Reversa (DRE) ---")
a.imprimirReverso(a.raiz)

print("\n")