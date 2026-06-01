from No import No


class Arvore:

    def __init__(self):
        self.raiz = None

    def inserir(self, raiz: No, valor):

        # cria o nó
        if raiz is None:
            nodo = No(valor)

            # define a raiz da árvore
            if self.raiz is None:
                self.raiz = nodo

            return nodo

        # esquerda
        if valor < raiz.dado:
            raiz.esq = self.inserir(raiz.esq, valor)

        # direita
        elif valor > raiz.dado:
            raiz.dir = self.inserir(raiz.dir, valor)

        return raiz

    # Em Ordem -> Esquerda / Raiz / Direita
    def imprimirEmOrdem(self, raiz: No):

        if raiz is not None:
            self.imprimirEmOrdem(raiz.esq)
            print(raiz.dado, end=" - ")
            self.imprimirEmOrdem(raiz.dir)

    # Pré Ordem -> Raiz / Esquerda / Direita
    def imprimirPreOrdem(self, raiz: No):

        if raiz is not None:
            print(raiz.dado, end=" - ")
            self.imprimirPreOrdem(raiz.esq)
            self.imprimirPreOrdem(raiz.dir)

    # Pós Ordem -> Esquerda / Direita / Raiz
    def imprimirPosOrdem(self, raiz: No):

        if raiz is not None:
            self.imprimirPosOrdem(raiz.esq)
            self.imprimirPosOrdem(raiz.dir)
            print(raiz.dado, end=" - ")

    # Ordem Reversa -> Direita / Raiz / Esquerda
    def imprimirReverso(self, raiz: No):

        if raiz is not None:
            self.imprimirReverso(raiz.dir)
            print(raiz.dado, end=" - ")
            self.imprimirReverso(raiz.esq)