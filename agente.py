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
        self.setPos(inicio)
        
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
                self.graficador.setCurrent(key)
                print("No cambio mi posición: ", key)
        
        # Refresca el mapa
        self.graficador.redrawMap()
            
    def move(self,destino):
        if (destino in self.vecinos):
            # Down
            self.ruta[pos[0]].append(destino)
            self.setPos(destino)
        elif (destino == ruta[actual][-1]):
            # Up
            
        
    #def startAgent(self):
        
    
    