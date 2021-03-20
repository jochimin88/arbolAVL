__author____ = 'Grupo IV'


class Nodo:

    def __init__(self, label):
        self.label = label
        self._padre = None
        self._izquierda = None
        self._derecha = None
        self.altura = 0

    @property
    def right(self):
        return self._derecha

    @right.setter
    def right(self, nodo):
        if nodo is not None:
            nodo._padre = self
            self._derecha = nodo

    @property
    def izquierda(self):
        return self._izquierda

    @izquierda.setter
    def izquierda(self, nodo):
        if nodo is not None:
            nodo._padre = self
            self._izquierda = nodo

    @property
    def parent(self):
        return self._padre

    @parent.setter
    def parent(self, nodo):
        if nodo is not None:
            self._padre = nodo
            self.altura = self.parent.altura + 1
        else:
            self.altura = 0
