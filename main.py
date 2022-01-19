
import threading
import time

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

class Agente:

    def __init__(self, mapa):
        self.mapa = mapa
        self.inicio = ""
        self.final = ""
        self.amplitud=False

    def setInicio(self, inicio):
        if (inicio in self.mapa):
            print("Ciudad inicial:", inicio)
            self.inicio = inicio
        else:
            print("No se encontro el inicio de la ruta en el mapa")
    
    def setFinal(self, final):
        if (final in self.mapa):
            print("Ciudad final:", final)
            self.final = final
        else:
            print("No se encontro el final de la ruta en el mapa")
    
    def setAmplitud(self):
        self.amplitud=True
    
    def setProfundidad(self):
        self.amplitud=False

    def Search(self):
        # Extrae el ultimo dato que se ingreso al buffer
        child = self.buffer_busqueda.pop()
        padre = self.padres.pop()
        #print("Pos_actual: ", self.pos, ", padre: ", self.padre)
        #print("explorando: ", child, ", padre: ", padre)
        print("\nRUTA ACTUAL: ", self.ruta)
        
        if (padre == self.pos):
            # Marca el lugar como visitado
            self.visitados.append(child)
            self.ruta.append(child)
            # Avanza el agente
            self.pos = child
            self.padre = padre
            print("AVANZO A: ", self.pos)
            
            if (self.pos==self.final):
                # Si ya llegué al destino final
                print("\nLlegué a: ",self.final)
                print(self.ruta)
                # Salgo de la función
                return True
            
            node_children = self.mapa[child].copy()
            # Si el nodo tiene hijos
            if len(node_children) != 0:
                for node_child in node_children:
                    # Solo agrega el nodo si es hijo y si no esta dentro de los lugares visitados
                    if (node_child != padre and node_child not in self.visitados):
                        if (self.amplitud):
                            # Agrega cada uno de los nodos hijos al inicio del buffer de busqueda
                            # FIFO
                            # Busqueda por amplitud
                            self.buffer_busqueda.insert(0,node_child)
                            self.padres.insert(0,child)
                        else:
                            # Agrega cada uno de los nodos hijos al final del buffer de busqueda
                            # LIFO
                            # Busqueda por profundidad
                            self.buffer_busqueda.append(node_child)
                            self.padres.append(child)
                #print("buffer: ",self.buffer_busqueda, "\n padres: ",self.padres,"\n visitados: ",self.visitados)
        else:
            if (self.padre != child):
                print("CAMBIO DE RAMA!")
                # Cambio de rama no esta permitido hasta que no regrese el agente
                # Regresa el dato al buffer
                self.buffer_busqueda.append(child)
                self.padres.append(padre)
                
                if (self.amplitud):
                    # Agrega cada uno de los nodos hijos al inicio del buffer de busqueda
                    # FIFO
                    # Busqueda por amplitud
                    self.buffer_busqueda.rinsert(0,"")
                    self.padres.insert(0,child)
                else:
                    # Retroceso en el mapa en busqueda por profundidad
                    index = listRightIndex(self.buffer_busqueda,child)+1
                    ruta = self.ruta.copy()
                    # Elimino el ultimo lugar de la ruta por que es donde me encuentro
                    ruta.pop()
                    # Agrego los lugares de la ruta por lo que pase anteriormente
                    # hasta llegar a un nodo antes del nodo padre de la rama a la 
                    # que quiero saltar
                    while ruta[-1] != padre:
                        l = ruta.pop()
                        p = ruta[-1]
                        self.buffer_busqueda.insert(index,l)
                        self.padres.insert(index,p)

                    # Agrega el nodo padre desde el que va a partir el agente de nuevo
                    l = ruta.pop()
                    if (len(ruta)>0):
                        p = ruta[-1]
                    else:
                        p = ""
                    self.buffer_busqueda.insert(index,l)
                    self.padres.insert(index,p)
                #print("buffer: ",self.buffer_busqueda, "\n padres: ",self.padres,"\n visitados: ",self.visitados)
                #print(self.ruta,"\n")
            else:
                self.pos = child
                self.padre = padre
                self.ruta.pop()
                print("RETROCEDI A: ", self.pos)
        #print(self.ruta,"\n")
        return False

    def runAgent(self):
        if (self.inicio != "" and self.final != ""):
            # Inicializa arreglos 
            self.visitados = []
            self.child = []
            self.buffer_busqueda = []
            self.anterior = ""
            self.ruta = []
            self.padres = []
            # Establece la posicion inicial
            self.pos = self.inicio
            self.padre = ""
            # Agrega el inicial a visitados para excluirlo de la busqueda
            self.visitados.append(self.pos)
            # Carga los vecinos del nodo inicial al buffer
            self.buffer_busqueda = self.mapa[self.pos].copy()
            self.padres= len(self.buffer_busqueda)*[self.pos]
            self.ruta.append(self.pos)
            # Realizará la busqueda mientras existan datos en el buffer
            while (len(self.buffer_busqueda)>0):
                time.sleep(0.2)
                if (self.Search()):
                    print("Busqueda terminada")
                    return
            
        else:
            print("Establezca inicio y final")
    
        


mapa = {"Arad":["Zerind","Sibiu","Timisoara"],
"Zerind":["Oradea"],
"Oradea":["Sibiu"],
"Timisoara":["Lugoj"],
"Lugoj":["Mehadia"],
"Mehadia":["Dobreta"],
"Dobreta":["Craiova"],
"Sibiu":["Rimnicu Vilcea","Fagaras"],
"Fagaras":["Bucharest"],
"Rimnicu Vilcea":["Pitesti","Craiova"],
"Craiova":["Pitesti"],
"Pitesti":["Bucharest"],
"Bucharest":["Giurgiu","Urziceni"],
"Urziceni":["Hirsova","Vaslui"],
"Vaslui":["Iasi"],
"Iasi":["Neamt"],
"Neamt":[],
"Hirsova":["Eforie"],
"Eforie":[]
}

mapa2 = {"Arad":["Sibiu","Timisoara","Zerind"],
"Zerind":["Oradea","Arad"],
"Oradea":["Zerind","Sibiu"],
"Timisoara":["Lugoj","Arad"],
"Lugoj":["Timisoara","Mehadia"],
"Dobreta":["Mehadia","Craiova"],
"Mehadia":["Lugoj","Dobreta"],
"Sibiu":["Fagaras","Rimnicu Vilcea","Arad","Oradea"],
"Fagaras":["Sibiu","Bucharest"],
"Rimnicu Vilcea":["Sibiu","Pitesti","Craiova"],
"Craiova":["Pitesti","Rimnicu Vilcea","Dobreta"],
"Pitesti":["Rimnicu Vilcea","Craiova","Bucharest"],
"Bucharest":["Fagaras","Pitesti","Giurgiu","Urziceni"],
"Urziceni":["Bucharest","Hirsova","Vaslui"],
"Vaslui":["Urziceni","Iasi"],
"Iasi":["Neamt","Vaslui"],
"Neamt":["Iasi"],
"Hirsova":["Urziceni","Eforie"],
"Eforie":["Hirsova"]
}

agent = Agente(mapa2)
agent.setInicio("Arad")
agent.setFinal("Eforie")
#agent.setAmplitud()
agent.runAgent()