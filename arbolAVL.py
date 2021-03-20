

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

# Declaramos la clase AVL


class AVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

        """
        Operación de inserción para agregar nuevos nodos
        al árbol.
        """

    def insertar(self, value):
        nodo = Nodo(value)

        if self.raiz is None:
            self.raiz = nodo
            self.raiz.altura = 0
            self.tamano = 1
        else:
            dad_nodo = None
            curr_nodo = self.raiz

            while True:
                if curr_nodo is not None:

                    dad_nodo = curr_nodo

                    if nodo.label < curr_nodo.label:
                        curr_nodo = curr_nodo.izquierda
                    else:
                        curr_nodo = curr_nodo.right
                else:
                    nodo.altura = dad_nodo.altura
                    dad_nodo.altura += 1
                    if nodo.label < dad_nodo.label:
                        dad_nodo.izquierda = nodo
                    else:
                        dad_nodo.right = nodo
                    self.rebalance(nodo)
                    self.tamano += 1
                    break

# Josue
        # Operación de rotación
    def rebalance(self, nodo):
        n = nodo

        while n is not None:
            altura_derecha = n.altura
            altura_izquierda = n.altura

            if n.right is not None:
                altura_derecha = n.right.altura

            if n.izquierda is not None:
                altura_izquierda = n.izquierda.altura

            if abs(altura_izquierda - altura_derecha) > 1:
                if altura_izquierda > altura_derecha:
                    izquierda_child = n.izquierda
                    if izquierda_child is not None:
                        h_derecha = (izquierda_child.right.altura
                                     if (izquierda_child.right is not None) else 0)
                        h_izquierda = (izquierda_child.izquierda.altura
                                       if (izquierda_child.izquierda is not None) else 0)
                    if (h_izquierda > h_derecha):
                        self.rotar_izquierda(n)
                        break
                    else:
                        self.double_rotar_derecha(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        h_derecha = (right_child.right.altura
                                     if (right_child.right is not None) else 0)
                        h_izquierda = (right_child.izquierda.altura
                                       if (right_child.izquierda is not None) else 0)
                    if (h_izquierda > h_derecha):
                        self.double_rotar_izquierda(n)
                        break
                    else:
                        self.rotar_derecha(n)
                        break
            n = n.parent

    def rotar_izquierda(self, nodo):
        aux = nodo.parent.label
        nodo.parent.label = nodo.label
        nodo.parent.right = Nodo(aux)
        nodo.parent.right.altura = nodo.parent.altura + 1
        nodo.parent.izquierda = nodo.right

    def rotar_derecha(self, nodo):
        aux = nodo.parent.label
        nodo.parent.label = nodo.label
        nodo.parent.izquierda = Nodo(aux)
        nodo.parent.izquierda.altura = nodo.parent.altura + 1
        nodo.parent.right = nodo.right

    def double_rotar_izquierda(self, nodo):
        self.rotar_derecha(nodo.getRight().getRight())
        self.rotar_izquierda(nodo)

    def double_rotar_derecha(self, nodo):
        self.rotar_izquierda(nodo.getizquierda().getizquierda())
        self.rotar_derecha(nodo)

    def vacio(self):
        if self.raiz is None:
            return True
        return False

    def preMuestra(self, curr_nodo):
        if curr_nodo is not None:
            self.preMuestra(curr_nodo.izquierda)
            print(curr_nodo.label, end=" ")
            self.preMuestra(curr_nodo.right)

    def preorder(self, curr_nodo):
        if curr_nodo is not None:
            self.preMuestra(curr_nodo.izquierda)
            self.preMuestra(curr_nodo.right)
            print(curr_nodo.label, end=" ")

    def obtenerRaiz(self):
        return self.raiz


if __name__ == '__main__':
    t = AVL()
    t.insertar(5)
    t.insertar(9)
    t.insertar(13)
    t.insertar(10)
    t.insertar(17)
    t.preMuestra(t.raiz)
