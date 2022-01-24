#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:23:17 2022

@author: miguel
"""
from graficador import Graficador 
from agente import Agente

mapa3={
"Arad":{"nodes":["Zerind","Sibiu","Timisoara"],"coord":[67,133]},
"Zerind":{"nodes":["Oradea","Arad"],"coord":[92,80]},
"Oradea":{"nodes":["Zerind","Sibiu"],"coord":[122,25]},
"Timisoara":{"nodes":["Lugoj","Arad"],"coord":[72,245]},
"Lugoj":{"nodes":["Timisoara","Mehadia"],"coord":[168,287]},
"Dobreta":{"nodes":["Mehadia","Craiova"],"coord":[169,395]},
#"Dobreta":{"nodes":["Mehadia"],"coord":[169,395]},
"Mehadia":{"nodes":["Lugoj","Dobreta"],"coord":[173,340]},
"Sibiu":{"nodes":["Arad","Oradea","Rimnicu Vilcea","Fagaras"],"coord":[227,181]},
"Fagaras":{"nodes":["Sibiu","Bucharest"],"coord":[362,191]},
"Rimnicu Vilcea":{"nodes":["Sibiu","Pitesti","Craiova"],"coord":[261,244]},
"Craiova":{"nodes":["Pitesti","Rimnicu Vilcea","Dobreta"],"coord":[287,410]},
#"Craiova":{"nodes":["Pitesti","Rimnicu Vilcea"],"coord":[287,410]},
"Pitesti":{"nodes":["Rimnicu Vilcea","Craiova","Bucharest"],"coord":[381,302]},
"Bucharest":{"nodes":["Fagaras","Pitesti","Giurgiu","Urziceni"],"coord":[488,356]},
"Urziceni":{"nodes":["Bucharest","Hirsova","Vaslui"],"coord":[565,325]},
"Vaslui":{"nodes":["Urziceni","Iasi"],"coord":[636,197]},
"Iasi":{"nodes":["Neamt","Vaslui"],"coord":[587,114]},
"Neamt":{"nodes":["Iasi"],"coord":[495,71]},
"Hirsova":{"nodes":["Urziceni","Eforie"],"coord":[669,326]},
"Eforie":{"nodes":["Hirsova"],"coord":[707,402]},
"Giurgiu":{"nodes":["Bucharest"],"coord":[453,433]}
}


graph = Graficador()
graph.loadMap(mapa3)
agent = Agente(graph)
agent.setInicio("Arad")
agent.setFinal("Bucharest")
agent.setBehavior('amplitud')                       
agent.runAgent()
input ("\n\nPresione una tecla para continuar ...")
#agent.setAmplitud()
# agent.moveTo('Zerind')
# time.sleep(0.1)
# agent.moveTo('Timisoara')
# time.sleep(0.1)
# agent.moveTo('Sibiu')
# time.sleep(0.1)
# agent.moveTo('Timisoara')
# agent.moveTo('Lugoj')
# time.sleep(0.1)
# agent.moveTo('Zerind')
# agent.moveTo('Oradea')
# time.sleep(0.1)
# agent.moveTo('Lugoj')
