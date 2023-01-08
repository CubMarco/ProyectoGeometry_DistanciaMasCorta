class Nodo:
    def __init__(self, fila, columna, other=None, father=None):
        self.fila = fila
        self.columna = columna
        self.c = 0
        self.d = 0
        self.h = 0
        self.hijos = []
        self.hijosVisitados = 0
        self.other = other
        self.father = father

    def toString(self):
        father = "raiz"
        if (self.father != None):
            father = "Father: " + str(self.father.valor)
        return "valor: (" + str(self.valor) + ")" + "other: " + self.other + " " + father


class Arbol:
    def __init__(self):
        self.__raiz = None

    def iniciar(self, fila, columna):
        self.__raiz = Nodo(fila, columna, "Punto inicial")
        return self.__raiz

    def insertar(self, fila, columna, nodoPadre, other=""):
        if (self.__raiz == None or nodoPadre.fila == ""):
            self.iniciar(fila, columna)
            return self.__raiz
        nodoHijo = Nodo(fila, columna, other, nodoPadre)
        nodoPadre.hijos.append(nodoHijo)
        return nodoHijo

    def imprimir(self, nodo=None, nodoPadre=None):
        if (nodo == None):
            nodo = self.__raiz

        if nodoPadre != None:
            print('padre: ', nodoPadre.valor)
        print(nodo.toString())
        for n in nodo.hijos:
            self.imprimir(n, nodo)

    def bfs(self, visited=[], node=None):
        if node == None:
            node = self.__raiz
        visited.append(node)
        queue = []
        queue.append(node)

        while queue:
            s = queue.pop(0)
            if s.other == "Punto final":
                camino = self.__getCamino__(s)
                print("camino: ", )
                for level in camino:
                    print(level.toString())
                return
            for neighbour in s.hijos:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def __getCamino__(self, nodo, camino=[]):
        camino.append(nodo)
        if (nodo.father == None):
            return camino
        return self.__getCamino__(nodo.father)