import busqueda


mapa2 = {"Arad":["Timisoara","Zerind","Sibiu"],
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
"Eforie":["Hirsova"],
"Giurgiu" :["Bucharest"],
}

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
"Eforie":[],
"Giurgiu" :[],
}



inicio = "Arad"
final = "Bucharest"
print("\nBusqueda de profundidad\n")
busqueda.profundidad(inicio,final,mapa)

print("\n\nBusqueda de amplitud\n")
busqueda.amplitud(inicio,final,mapa)