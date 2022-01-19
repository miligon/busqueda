def Search(inicio, final, mapa, amplitud=False):
    if (inicio in mapa and final in mapa):
        print("Iniciando en:", mapa[inicio])
    else:
        print("No se encontro el inicio o el final de la ruta en el mapa")
        return
    
    # Inicializa arreglos
    visitados = []
    child = []
    buffer_busqueda = []
    padres = []

    # Establece la posicion inicial
    pos = inicio
    # Agrega el inicial a visitados para excluirlo de la busqueda
    visitados.append(pos)
    # Carga los vecinos del nodo inicial al buffer
    buffer_busqueda = mapa[pos].copy()
    padres= len(buffer_busqueda)*[pos]
    print(padres, buffer_busqueda)
    # Realizará la busqueda mientras existan datos en el buffer
    while (len(buffer_busqueda)>0):
        #print(mapa)
        # Extrae el ultimo dato que se ingreso al buffer
        child = buffer_busqueda.pop()
        padre = padres.pop()
        print("Nodo: ", padre, ", Explorando: ", child)

        if child not in visitados:
            # Marca el lugar como visitado
            visitados.append(child)
            # Avanza al nuevo hijo
            pos = child
            
            if (pos==final):
                # Si ya llegué al destino final
                print("Llegué a: ",final)
                print(visitados)
                # Salgo de la función
                return
            
            node_children = mapa[child].copy()
            # Si el nodo tiene hijos
            if len(node_children) != 0:
                for node_child in node_children:
                    if (amplitud):
                        # Agrega cada uno de los nodos hijos al inicio del buffer de busqueda
                        # FIFO
                        # Busqueda por amplitud
                        buffer_busqueda.insert(0,node_child)
                        padres.insert(0,child)
                    else:
                        # Agrega cada uno de los nodos hijos al final del buffer de busqueda
                        # LIFO
                        # Busqueda por profundida
                        buffer_busqueda.append(node_child)
                        padres.append(child)
        else:
            print("visitado anteriormente: ", child)

    print("Busqueda terminada")

def amplitud(inicio,final,mapa):
    Search(inicio,final,mapa,True)

def profundidad(inicio,final,mapa):
    Search(inicio,final,mapa)