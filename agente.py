#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:23:17 2022

@author: miguel
"""


class Agente:
    def __init__(self, graficador):
        self.graficador = graficador
        self.inicio = ""
        self.final = ""
        self.posicion_actual = [0,0] # ruta, profundidad
        self.ruta = [[""]]
        self.ruta_actual = 0
        self.visitados = []
        self.vecinos = []
        self.modoBusqueda = 'profundidad'
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
            print("1y")
            if ( len(self.ruta[pos[0]]) == (pos[1]+1) ):
                # Nuevo nodo
                self.ruta[pos[0]].append(destino)
                print("agregue: ", destino)
            new_pos = [pos[0],(pos[1] + 1)]  
            self.setPos(new_pos)
            return True
        else:
            print("1n")
            if(pos[1] > 0):
                print(2)
                if (destino == self.ruta[pos[0]][pos[1]-1]):
                    # Up
                    print(3)
                    new_pos = [pos[0],(pos[1] - 1)]  
                    self.setPos(new_pos)
                    return True
        return False
                
            
        
    #def startAgent(self):
        
    
    