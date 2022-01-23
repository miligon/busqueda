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
        self.posicion_actual = ""
        self.posicion_anterior= ""
        self.ruta = [[],[]]
        self.visitados = []
        self.vecinos = []
        print("Agente creado!")

    def setInicio(self, inicio):
        print("Ciudad inicial:", inicio)
        self.inicio = inicio
        self.setPos(inicio)
        #self.posicion_actual = [self.inicio, 'inicio']
        # Agrega el inicial a visitados para excluirlo de la busqueda
        #self.visitados.append(self.inicio)
        #self.buffer_busqueda = self.mapa[self.pos].copy()
        #self.padres= len(self.buffer_busqueda)*[self.pos]
        #self.ruta.append(self.pos)
        
    def setFinal(self, final):
        print("Ciudad final:", final)
        self.final = final
    
    def setBehavior(self,modo):
        if (modo == 'amplitud'):
            self.modoBusqueda = 'amplitud'
        else:
            self.modoBusqueda = 'profundidad'
      
    def setPos(self,key):
        if (key != self.posicion_actual):
            posicion_anterior = self.posicion_actual
            self.posicion_actual = key
            if ( posicion_anterior != "" ):
                if (posicion_anterior not in self.visitados):
                    self.visitados.append(posicion_anterior)
                self.graficador.setVisited(posicion_anterior)
            self.vecinos = self.graficador.getNodes(key)
            self.graficador.setCurrent(key)
            print("Nueva posicion: ", key)
        
        else:
            if (key == self.posicion_actual):
                self.graficador.setCurrent(key)
                print("No cambio mi posición: ", key)
        
        # Refresca el mapa
        self.graficador.redrawMap()
            
    #def moveTo(self,key):
        
    #def startAgent(self):
        
    
    