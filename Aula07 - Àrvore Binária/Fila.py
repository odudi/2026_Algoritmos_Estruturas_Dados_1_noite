from No import No
from NoFila import NoFila   

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, NoDarvore):
        nodo = NoFila(NoDarvore)
        if self.inicio is None:
            self.inicio = nodo

        else:
            self.fim.prox = nodo
        self.fim = nodo

    def remover(self):
        aux = self.inicio.noArvore
        if self.inicio is not None:
            
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None 
        return aux.dado
   