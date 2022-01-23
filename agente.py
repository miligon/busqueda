#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:23:17 2022

@author: miguel
"""
import time

class Agente:
    def __init__(self, graficador):
        self.graficador = graficador
        self.inicio = ""
        self.final = ""
        self.posicion_actual = [0,0] # ruta, profundidad
        self.ruta = [[""]]
        self.visitados = []
        self.vecinos = []
        self.modoBusqueda = 'profundidad'
        self.buffer_busqueda = []
        print("Agente creado!")

    def setInicio(self, inicio):
        print("Ciudad inicial:", inicio)
        self.inicio = inicio
        self.ruta = [[inicio]]
        self.setPos([0,0])
        
    def setFinal(self, final):
        print("Ciudad final:", final)
        self.final = final
    
    def setBehavior(self,modo):
        if (modo == 'amplitud'):
            self.modoBusqueda = 'amplitud'
        else:
            self.modoBusqueda = 'profundidad'
      
    def setPos(self,pos):
        if (pos != self.posicion_actual):
            pos_ant = self.posicion_actual
            self.posicion_actual = pos
            key = self.ruta[pos[0]][pos[1]]
            key_anterior = self.ruta[pos_ant[0]][pos_ant[1]]
            if (key_anterior not in self.visitados):
                self.visitados.append(key_anterior)
            self.graficador.setVisited(key_anterior)
            self.vecinos = self.graficador.getNodes(key)
            self.graficador.setCurrent(key)
            print("Nueva posicion: ", key)
        
        else:
            if (pos == self.posicion_actual):
                key = self.ruta[pos[0]][pos[1]]
                self.vecinos = self.graficador.getNodes(key)
                self.graficador.setCurrent(key)
                print("No cambio mi posición: ", key)
        
        # Refresca el mapa
        self.graficador.redrawMap()
            
    def move(self,destino):
        pos = self.posicion_actual
        if (destino in self.vecinos and destino not in self.ruta[pos[0]]):
            # Down
            if ( len(self.ruta[pos[0]]) == (pos[1]+1) ):
                # Dive in to node
                self.ruta[pos[0]].append(destino)
                print("agregue: ", destino)
            new_pos = [pos[0],(pos[1] + 1)]  
            self.setPos(new_pos)
            return True
        else:
            if(pos[1] > 0):
                if (destino == self.ruta[pos[0]][pos[1]-1]):
                    # Up
                    new_pos = [pos[0],(pos[1] - 1)]  
                    self.setPos(new_pos)
                    return True
        return False
    
    def moveTo(self, destino):
        if (destino not in self.vecinos and
            destino not in self.ruta[self.posicion_actual[0]]):
            # Cambio de rama, buscar el nodo que tiene como vecino a destino
            while (destino not in self.vecinos):
                print(99)
                time.sleep(0.5)
                if (self.posicion_actual[1]>0):
                    new_depth = self.posicion_actual[1]-1
                    key = self.ruta[self.posicion_actual[0]][new_depth]
                    print("regresando a:", key)
                    self.move(key)
                else:
                    print("Llegue a inicio sin encontrar la rama")
                    return False
                
            if (destino in self.vecinos):
                print("CAMBIANDO A NUEVA RUTA :D")
                
                depth_i = self.posicion_actual[1] + 1
                route = self.posicion_actual[0]
                self.ruta.append(self.ruta[route][:depth_i])
                self.posicion_actual[0] = route + 1
                self.move(destino)
        else:
            if (destino in self.vecinos):
                self.move(destino)
                
            
    def runSearch(self):
        self.buffer_busqueda = self.vecinos.copy()
        while(len(self.buffer_busqueda)>0):
            try_node = self.buffer_busqueda.pop()
            self.moveTo(try_node)
            time.sleep(0.5)
            if (self.final == try_node):
                print("Llegué a:", try_node)
                return self.ruta[self.posicion_actual[0]]
            
            nodes = self.vecinos.copy()
            if len(nodes) != 0:
                for child in nodes:
                    if (child not in self.visitados):
                        #self.buffer_busqueda.append(child)
                        self.buffer_busqueda.insert(0,child)
                        print(try_node)
            
        
    
    