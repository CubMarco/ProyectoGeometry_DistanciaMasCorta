import turtle
import time
from arbol import Arbol

arbol= Arbol()
# Configuracion ventana
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Proyecto Final")
wn.setup(700, 700)
wn.tracer(0)

#///////////// Clases de agentes ///////////////
class Humano():
    def __init__(self):
        self.color = "pink"
        self.montana = -1
        self.tierra = 1
        self.agua = 2
        self.arena = 3
        self.bosque = 4
        self.lodo = 5
        self.nieve = 5

class Mono():
    def __init__(self):
        self.color = "dark goldenrod"
        self.montana = -1
        self.tierra = 2
        self.agua = 4
        self.arena = 3
        self.bosque = 1
        self.lodo = 5
        self.nieve = -1

class Pulpo():
    def __init__(self):
        self.color = "SteelBlue1"
        self.montana = -1
        self.tierra = 2
        self.agua = 1
        self.arena = 3
        self.bosque = 4
        self.lodo = 2
        self.nieve = 4

#///////////// Clases de terreno ///////////////
class Pasto(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Agua(turtle.Turtle):
    def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)

class Montana(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Arena(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class Tierra(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("brown")
        self.penup()
        self.speed(0)

class Pantano(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)

class Camino(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Muro(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Meta(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#///////////// Crea el laberinto a partir de un txt ///////////////
nivel_2 = [] #se guardara el laberinto
cadena = [] #cadena auxiliar
fichero = open('laberinto.txt', 'r') #Se abre el archivo en lectura
for i in range(17): #Se recorreran las 16 lineas del laberinto
    texto = str(fichero.readline()) #Lee una linea del archivo y lo convertimos en string
    cadena.append(texto) #Añadimos el string al arreglo auxiliar
    nivel_2.append(cadena) #Añadimos la cadena
for nivel_2 in nivel_2: #for que recorre el nivel_2
    pass #No hace nada
fichero.close() #Se cierra el archivo

tierra = Tierra()
agua = Agua()
montana = Montana()
arena = Arena()
pasto = Pasto()
pantano = Pantano()
#camino=Camino()
muro=Muro()
meta=Meta()

def mostrar(fila, columna):
    entorno = nivel_2[fila][columna]
    screen_x = -180 + (columna * 24)
    screen_y = 180 - (fila * 24)
    if entorno == "0":
        montana.goto(screen_x, screen_y)
        montana.stamp()
    if entorno == "1":
        tierra.goto(screen_x, screen_y)
        tierra.stamp()
    if entorno == "2":
        agua.goto(screen_x, screen_y)
        agua.stamp()
    if entorno == "3":
        arena.goto(screen_x, screen_y)
        arena.stamp()
    if entorno == "4":
        pasto.goto(screen_x, screen_y)
        pasto.stamp()
    if entorno == "5":
        pantano.goto(screen_x, screen_y)
        pantano.stamp()
    if entorno == "7":
        muro.goto(screen_x, screen_y)
        muro.stamp()
    if entorno == "9":
        meta.goto(screen_x, screen_y)
        meta.stamp()

# Persona
persona = turtle.Turtle()
persona.speed(0)
persona.shape("circle")
persona.penup()
#persona.goto(xinicio, yinicio)
persona.direction = "stop"

for m in range(17):
    for n in range(17):
        mostrar(m,n)
wn.update()

# Movimiento
def arriba():
    persona.direction = "up"

def abajo():
    persona.direction = "down"

def derecha():
    persona.direction = "right"

def izquierda():
    persona.direction = "left"

def mover_Lab(fila,columna,fila_or,columna_or):
    global decision
    if fila > fila_or: #si el valor actual de x es mayor de donde vino, se mueve a la derecha
        abajo()
    if fila_or > fila: #Por el contrario se movera a la izquierda
        arriba()
    if columna > columna_or:
        derecha()
    if columna_or > columna:
        izquierda()
    if persona.direction == "right":
        x = persona.xcor()
        persona.setx(x + 24)
        persona.direction = "stop"

    if persona.direction == "left":
        x = persona.xcor()
        persona.setx(x - 24)
        persona.direction = "stop"

    if persona.direction == "up":
        y = persona.ycor()
        persona.sety(y + 24)
        persona.direction = "stop"

    if persona.direction == "down":
        y = persona.ycor()
        persona.sety(y - 24)
        persona.direction = "stop"
    #mostrar(fila, columna)

def imprimirNumeros():
    text = turtle.Turtle()  # Esta parte de text es solo para escribir una V en el lugar donde esta el jugador
    text.speed(0)
    text.color("white")
    text.penup()
    text.hideturtle()

    for i in range(1,16):
        x_cor = -204 + ((0 + 1) * 24)
        y_cor = 204 - ((i + 1) * 24)
        text.goto(x_cor - 6, y_cor - 5)
        text.write(str(i), font=("Verdana",7, "normal"))

    for i in range(16):
        x_cor = -204 + ((i + 1) * 24)
        y_cor = 204 - ((0 + 1) * 24)
        text.goto(x_cor - 4, y_cor)
        text.write(str(i), font=("Verdana",7, "normal"))
    wn.update()

imprimirNumeros()

#///////Por el momento no se usa///////
def Es_Meta(fila, columna, filaMeta, columnaMeta):
    valor = False

    if fila == filaMeta:
        if columna == columnaMeta:
            valor = True
        else:
            valor = False
    else:
        valor = False
    return valor

#///////////// Calcula la distancia Manhattan entre dos puntos ///////////////
def distanciaManhattan(p1, p2, q1, q2):
    d = abs(p1 - q1) + abs(p2 - q2)
    return d

#///////////// Dependiendo del aegente, se obtiene el costo de cierto terreno ///////////////
def conocerCosto(agente, terreno):
    costo = 0
    if terreno == "0":
        costo = agente.montana
    if terreno == "1":
        costo = agente.tierra
    if terreno == "2":
        costo = agente.agua
    if terreno == "3":
        costo = agente.arena
    if terreno == "4":
        costo = agente.bosque
    if terreno == "5":
        costo = agente.lodo
    if terreno == "6":
        costo = agente.nieve
    return costo

#///////////// Encuentra un nodo en listaCerrados ///////////////
def encontrar_EnCerrados(nodo):
    fila = nodo.fila
    columna = nodo.columna
    for pos in range(len(listaCerrados)):
        if listaCerrados[pos].fila == fila and listaCerrados[pos].columna == columna:
            return True
    return False

#///////////// Encuentra un nodo en listaAbiertos ///////////////
def encontrar_EnAbiertos(nodo):
    fila = nodo.fila
    columna = nodo.columna
    h = nodo.h
    cambiado = False
    for pos in range(len(listaAbiertos)):
        if listaAbiertos[pos].fila == fila and listaAbiertos[pos].columna == columna:
            if h < listaAbiertos[pos].h:
                listaAbiertos[pos] = nodo
                cambiado = True
    if not(cambiado):
        listaAbiertos.append(nodo)
    return

#///////////// Genera los hijos que puede ///////////////
def generarHijos(nivel, nodo, agente, filaMeta, columnaMeta):
    #Tomamos los valores del nodo actual
    fila = nodo.fila
    columna = nodo.columna
    costoPadre = nodo.c
    h = 2147483640  # La distancia manhattan no puede ser mayor a esto

    #********** Revisa por la derecha, izquierda, arriba y abajo el terreno *******
    #********** Si en esa direccion no es el fin del mapa y no se ha visitado ******
    #********** Entonces se genera un hijo siempre y cuando su costo lo permita******
    if nivel[fila][columna + 1] != "7":  # Revisa por la derecha
        costo = conocerCosto(agente, nivel[fila][columna + 1])
        if costo != -1: #Si el agente si puede estar en esa casilla
            d = distanciaManhattan(fila, columna + 1, filaMeta, columnaMeta)
            nodoDerecha = arbol.insertar(fila, columna + 1, nodo, "Hoja") #Se crea el nodo
            nodoDerecha.c = costo + costoPadre #Acumula el costo del padre con el camino a seguir
            nodoDerecha.d = d
            nodoDerecha.h = costo + costoPadre + d
            if not(encontrar_EnCerrados(nodoDerecha)):
                encontrar_EnAbiertos(nodoDerecha)

    if nivel[fila][columna - 1] != "7":  # Revisa por la izquierda
        costo = conocerCosto(agente, nivel[fila][columna - 1])
        if costo != -1: #Si el agente si puede estar en esa casilla
            d = distanciaManhattan(fila, columna - 1, filaMeta, columnaMeta)
            nodoIzquierdo = arbol.insertar(fila, columna - 1, nodo, "Hoja")
            nodoIzquierdo.c = costo + costoPadre
            nodoIzquierdo.d = d
            nodoIzquierdo.h = costo + costoPadre + d
            if not (encontrar_EnCerrados(nodoIzquierdo)):
                encontrar_EnAbiertos(nodoIzquierdo)

    if nivel[fila + 1][columna] != "7":  # Revisa por abajo
        costo = conocerCosto(agente, nivel[fila + 1][columna])
        if costo != -1:
            d = distanciaManhattan(fila + 1, columna, filaMeta, columnaMeta)
            nodoAbajo = arbol.insertar(fila + 1, columna, nodo, "Hoja")
            nodoAbajo.c = costo + costoPadre
            nodoAbajo.d = d
            nodoAbajo.h = costo + costoPadre + d
            if not (encontrar_EnCerrados(nodoAbajo)):
                encontrar_EnAbiertos(nodoAbajo)

    if nivel[fila - 1][columna] != "7":  # Revisa por arriba
        costo = conocerCosto(agente, nivel[fila - 1][columna])
        if costo != -1:
            d = distanciaManhattan(fila - 1, columna, filaMeta, columnaMeta)
            nodoArriba = arbol.insertar(fila - 1, columna, nodo, "Hoja")
            nodoArriba.c = costo + costoPadre
            nodoArriba.d = d
            nodoArriba.h = costo + costoPadre + d
            if not (encontrar_EnCerrados(nodoArriba)):
                encontrar_EnAbiertos(nodoArriba)
    #Regresa al nodo que obtuvo la menor distancia con el menor costo
    return

visited = [[0 for fila in range(16)] for columna in range(16)]
ruta = [[]]
#////////////////////////////// Programacion Algoritmo A* //////////////////////////////
listaAbiertos = [] #Guardara los nodos no explorados
listaCerrados = [] #Guardara los nodos que ya fueron explorados

def algoritmo_A(nivel, agente, fila, columna, filaMeta, columnaMeta):
    nodo = arbol.iniciar(fila, columna)
    nodo.c = 0
    nodo.h = nodo.d = distanciaManhattan(fila, columna, filaMeta, columnaMeta)
    listaCerrados.append(nodo)
    generarHijos(nivel, nodo, agente, filaMeta, columnaMeta)  # Ahora 'nodo' es uno de sus hijos
    nodo = listaAbiertos[0]
    for i in range(len(listaAbiertos)):
        if listaAbiertos[i].h <= nodo.h:
            nodo = listaAbiertos[i]
    fila = nodo.fila
    columna = nodo.columna

    #El ciclo se hara siempre que no llegue a la meta y que exista
    #al menos un elemento en listaAbiertos
    while not(Es_Meta(fila,columna,filaMeta, columnaMeta)) and listaAbiertos:
        generarHijos(nivel, nodo, agente, filaMeta, columnaMeta)  # Ahora 'nodo' es uno de sus hijos
        listaCerrados.append(nodo)
        listaAbiertos.remove(nodo)
        nodo = listaAbiertos[0]
        for i in range(len(listaAbiertos)):
            if listaAbiertos[i].h <= nodo.h:
                nodo = listaAbiertos[i]
        fila = nodo.fila
        columna = nodo.columna
        #print(f"Nodo Actual fila:{nodoHijo.fila}, columna:{nodoHijo.columna}, h: {nodoHijo.h}")

    if listaAbiertos:
        return nodo
    else:
        print("\n El laberinto no tiene solucion")

#////////////////////////////// Fin Algoritmo A* //////////////////////////////

#********* Imprime la ruta optima, parte de la hoja hasta la raiz *********
def mostrarCamino (nodo):
    if nodo != None:
        fila = nodo.fila
        columna = nodo.columna
        mostrarCamino(nodo.father)
    else:
        return
    print("[",fila,",",columna,"]")
    ruta.append([fila, columna])

    return

def mostrarPantalla(ruta):
    mover_Lab(ruta[0][0], ruta[0][1], ruta[0][0], ruta[0][1])
    wn.update()
    time.sleep(1)
    for i in range(1, len(ruta)):
        fila = ruta[i][0]
        columna = ruta[i][1]
        filaOr = ruta[i - 1][0]
        columnaOr = ruta[i - 1][1]
        mover_Lab(fila, columna, filaOr, columnaOr)
        wn.update()
        time.sleep(1)

#*************** Main del programa **************
if __name__ == '__main__':
    #Se le pregunta al usuario que clase de agente desea
    tipo = int(input("Seleccione un agente\n1)Humano\n2)Mono\n3)Pulpo\n"))
    if tipo == 1:
        tipo = Humano()
    if tipo == 2:
        tipo = Mono()
    if tipo == 3:
        tipo = Pulpo()
    persona.color(tipo.color)

    modo = int(input("Seleccione un modo\n1)Destino Unico\n2)Varios destinos\n"))
    if modo == 1:
        filaInicio = int(input("Fila para empezar: "))
        columnaInicio = int(input("Columna para empezar: "))
        #Si los valores del inicio son una casilla que el agente no puede visitar, se termina
        if conocerCosto(tipo, nivel_2[filaInicio][columnaInicio]) == -1:
            print("El agente no tiene permitido empezar aqui")
            exit()
        mostrar(filaInicio, columnaInicio)  # Mostramos en pantalla la meta
        # Para mostrar al agente se le suma 1, ya que tanto la primer y última
        # columna son 7, los cuáles no contemos, además de las filas
        xinicio = -204 + ((columnaInicio + 1) * 24)
        yinicio = 204 - ((filaInicio + 1) * 24)
        persona.goto(xinicio, yinicio)
        filaMeta = int(input("Fila final: "))
        columnaMeta = int(input("Columna final: "))
        # Si los valores del final son una casilla que el agente no puede visitar, se termina
        if conocerCosto(tipo, nivel_2[filaMeta][columnaMeta]) == -1:
            print("El agente no puede llegar ahi porque no tiene acceso a el")
            exit()
        mostrar(filaMeta, columnaMeta) #Mostramos en pantalla la meta
        meta = algoritmo_A(nivel_2, tipo, filaInicio, columnaInicio, filaMeta, columnaMeta)
        #imprimirLetras()
        print("\nRuta optima")
        #Muestra el reocorrido que realizo el agente
        mostrarCamino(meta)
        try:
            ruta.remove([])
        except ValueError:
            pass  # do nothing!
        mostrarPantalla(ruta)
        input()
    if modo == 2:
        #Aqui se ha esocgido que habran multiples metas
        filaInicio = int(input("Fila para empezar: "))
        columnaInicio = int(input("Columna para empezar: "))
        if conocerCosto(tipo, nivel_2[filaInicio][columnaInicio]) == -1:
            print("El agente no tiene permitido empezar aqui")
            exit()
        #Para mostrar al agente se le suma 1, ya que tanto la primer y última
        #columna son 7, los cuáles no contemos, además de las filas
        xinicio = -204 + ((columnaInicio + 1) * 24)
        yinicio = 204 - ((filaInicio + 1) * 24)
        persona.goto(xinicio, yinicio)
        n = int(input("Cantidad de destinos: "))
        fMeta = [0 for filaInicio in range(225)]
        cMeta = [0 for columnaInicio in range(225)]
        #Se le pedira al usuario que ingrese tanto la fila como la columna
        #De cada uno de los destinos
        for i in range(n):
            fMeta[i] = int(input("Fila Meta: "))
            cMeta[i] = int(input("Columna Meta: "))
            if conocerCosto(tipo, nivel_2[fMeta[i]][cMeta[i]]) == -1:
                print("El agente no puede llegar ahi porque no tiene acceso a el")
                exit()
        costoTotal = 0
        #Realizara al algoritmo n cantidad de veces
        for j in range(n):
            meta = algoritmo_A(nivel_2, tipo, filaInicio, columnaInicio, fMeta[j], cMeta[j])
            costoTotal += meta.c
            #Para llegar al otro objetivo es necesario que el inicio sea
            #los valores de la meta del anterior algoritmo
            filaInicio = fMeta[j]
            columnaInicio = cMeta[j]
            print("\nRuta optima")
            mostrarCamino(meta)
            #imprimirLetras()
            listaCerrados.clear()
            listaAbiertos.clear()
        try:
            ruta.remove([])
        except ValueError:
            pass  # do nothing!
        mostrarPantalla(ruta)
        #print(f"\nCosto Total: {costoTotal}")
