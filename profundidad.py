def DepthSearch(inicio, final, mapa):
    if (inicio in mapa and final in mapa):
        print("Iniciando en:", mapa[inicio])
    else:
        print("No se encontro el inicio o el final de la ruta en el mapa")
        return
    
    # Inicializa arreglos
    visitados = []
    child = []
    buffer_busqueda = []

    # Establece la posicion inicial
    pos = inicio
    # Agrega el inicial a visitados para excluirlo de la busqueda
    visitados.append(pos)
    # Carga los vecinos del nodo inicial al buffer
    buffer_busqueda = mapa[pos]
    # Realizará la busqueda mientras existan valores en el buffer
    while (len(buffer_busqueda)>0):
        # Extrae el ultimo valor que se ingreso al buffer
        child = buffer_busqueda.pop()
        print("Explorando: ", child)

        if child not in visitados:
            # Marca el lugar como visitado
            visitados.append(child)
            pos = child
            
            if (pos==final):
                # Si ya llegué al destino final
                print("Llegué a: ",final)
                print(visitados)
                # Salgo y regreso la ruta
                return visitados
            
            try:
                # Si el nodo tiene hijos
                if len(mapa[child]) != 0:
                    for node_child in mapa[child]:
                        # Y no son nodos hijos que ya se visitaron
                        if node_child not in visitados:
                            # Agrega cada uno de los nodos hijos al final del buffer de busqueda
                            buffer_busqueda.append(node_child)
                        
            except(KeyError):
                continue 

    print("Busqueda terminada")