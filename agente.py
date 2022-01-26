#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:23:17 2022

@author: miguel
"""
import time
import threading


class Agente:
    def __init__(self, id):
        self.id = id
        self.inicio = ""
        self.final = ""
        self.posicion_actual = [0, 0]  # ruta, profundidad
        self.prev_pos = ""
        self.cambios_de_ruta = [[],[]]
        self.ruta = [[""]]
        self.visitados = []
        self.vecinos = []
        self.modoBusqueda = 'profundidad'
        self.buffer_busqueda = []
        self.padres = []
        self.movimientos = []
        self.state = 'idle'
        print("Agente creado!")

    def reset(self):
        self.inicio = ""
        self.final = ""
        self.posicion_actual = [0, 0]  # ruta, profundidad
        self.prev_pos = ""
        self.cambios_de_ruta = [[],[]]
        self.ruta = [[""]]
        self.visitados = []
        self.vecinos = []
        self.modoBusqueda = 'profundidad'
        self.buffer_busqueda = []
        self.padres = []
        self.movimientos = []
        self.state = 'idle'
        print("Agente reinicializado!")
        
    def getFinalRoute(self):
        if (self.state == 'finished'):
            return self.ruta[self.posicion_actual[0]]
        return False
    
    def getCurPos(self):
        return self.ruta[self.posicion_actual[0]][self.posicion_actual[1]]
    
    def getPrevPos(self):
        return self.prev_pos
        
    def setInicio(self, inicio, vecinos):
        print("Ciudad inicial:", inicio)
        print("Vecinos:", vecinos)
        self.setNewVecinos(vecinos)
        self.inicio = inicio
        self.ruta = [[inicio]]
        self.setPos([0, 0])
        self.buffer_busqueda = self.vecinos.copy()
        self.padres = len(self.buffer_busqueda) * [self.inicio]

    def setFinal(self, final):
        print("Ciudad final:", final)
        self.final = final

    def setBehavior(self, modo):
        if (modo == 'amplitud'):
            self.modoBusqueda = 'amplitud'
        else:
            self.modoBusqueda = 'profundidad'
            
    def setNewVecinos(self,vecinos):
        self.vecinos = vecinos

    def setPos(self, pos):
        if (pos != self.posicion_actual):
            pos_ant = self.posicion_actual
            self.posicion_actual = pos
            key = self.ruta[pos[0]][pos[1]]
            key_anterior = self.ruta[pos_ant[0]][pos_ant[1]]
            #Mantiene un registro unico de lugares visitados
            if (key_anterior not in self.visitados):
                self.visitados.append(key_anterior)
            self.prev_pos = key_anterior
            self.vecinos = []
            self.state = "waiting for nodes"
            print("Nueva posicion: ", key)

        else:
            if (pos == self.posicion_actual):
                key = self.ruta[pos[0]][pos[1]]
                self.state = "idle"
                print("No cambio mi posición: ", key)


    def move(self, destino):
        self.state = 'moving'
        print("Moviendo a: ", destino)
        pos = self.posicion_actual
        if (destino in self.vecinos and destino not in self.ruta[pos[0]]):
            # Down
            if (len(self.ruta[pos[0]]) == (pos[1]+1)):
                # Dive in to node
                self.ruta[pos[0]].append(destino)
                #print("agregue: ", destino)
            new_pos = [pos[0], (pos[1] + 1)]
            self.setPos(new_pos)
            return True
        
        if(pos[1] > 0):
            if (destino == self.ruta[pos[0]][pos[1]-1]):
                # Up
                new_pos = [pos[0], (pos[1] - 1)]
                self.setPos(new_pos)
                return True
        
        if(pos[1]+1 < len(self.ruta[pos[0]])):
            if (destino == self.ruta[pos[0]][pos[1]+1]):
                # Down existente
                new_pos = [pos[0], (pos[1] + 1)]
                self.setPos(new_pos)
                return True
        return False
    
    def moveTo(self, destino):
        self.state = 'calculating'
        print("Calculando movimientos ...")
        if (destino not in self.vecinos and
                destino not in self.ruta[self.posicion_actual[0]]):
            
            # Cambio de rama, buscar el nodo que tiene como vecino a destino
            while (destino not in self.vecinos):
                if (self.posicion_actual[1] > 0):
                    new_depth = self.posicion_actual[1]-1
                    key = self.ruta[self.posicion_actual[0]][new_depth]
                    #print("regresando a:", key)
                    #self.move(key)
                    self.movimientos.insert(0,key)
                else:
                    #print("Llegue a inicio sin encontrar la rama")
                    self.state = "idle"
                    return False
                
                if (destino not in self.vecinos):
                    for route in self.ruta:
                        depth_i = self.posicion_actual[1]
                        key = self.ruta[self.posicion_actual[0]][depth_i]
                        # Verifica si en la ciudad actual existen bifurcaciones
                        # y si el destino se encuentre en dichas bifurcaciones
                        if ((depth_i+1) < len(route)):
                            if (key == route[depth_i] and destino in route[depth_i+1:]):
                                #print("Cambiando a ruta existente")
                                route_num = self.ruta.index(route)
                                self.posicion_actual[0]=route_num
                                self.moveTo(destino)
                                return

            if (destino in self.vecinos):
                # Si el destino se encuentra en los vecinos de la ciudad
                # Se crea una nueva ruta
                #print("CAMBIANDO A NUEVA RUTA :D")
                depth_i = self.posicion_actual[1] + 1
                route = self.posicion_actual[0]
                nueva_ruta = self.ruta[route][:depth_i]
                self.ruta.append(nueva_ruta)
                self.posicion_actual[0] = route + 1                    
                #self.move(destino)
                self.movimientos.insert(0,destino)
                self.state = "idle"
        else:
            if (destino in self.vecinos):
                #self.move(destino)
                self.movimientos.insert(0,destino)
                self.state = "idle"
            else:
                if (destino in self.ruta[self.posicion_actual[0]]):
                    # Descender en una ruta en la que se encuentra el destino
                    while (destino not in self.vecinos):
                        if (self.posicion_actual[1] < (len(self.ruta[self.posicion_actual[0]])-1)):
                            new_depth = self.posicion_actual[1]+1
                            key = self.ruta[self.posicion_actual[0]][new_depth]
                            #print("avanzando a:", key)
                            #self.move(key)
                            self.movimientos.insert(0,key)
                        else:
                            #print("Llegue a inicio sin encontrar la rama")
                            self.state = "idle"
                            return False
                    #self.move(destino)
                    self.movimientos.insert(0,destino)
                    self.state = "idle"

    def runSearch(self):
        if (self.state == 'idle'):
            if ( len(self.movimientos) > 0 ):
                self.move(self.movimientos.pop())
                
                if (self.final == self.getCurPos()):
                    print("ENCONTRE: ", self.getCurPos())
                    self.state = 'finished'
                    return
                    
            else:
                if ( len(self.buffer_busqueda) > 0):
                    try_node = self.buffer_busqueda.pop()
                    padre = self.padres.pop()
                    
                    if (padre not in self.ruta[self.posicion_actual[0]]):
                        self.moveTo(padre)
                    self.moveTo(try_node)
        
                    nodes = self.vecinos.copy()
                    if len(nodes) != 0:
                        for child in nodes:
                            if (child not in self.visitados and child != padre):
                                if (self.modoBusqueda == 'amplitud'):
                                    self.buffer_busqueda.insert(0, child)
                                    self.padres.insert(0,try_node)
                                    
                                else:
                                    self.buffer_busqueda.append(child)
                                    self.padres.append(try_node)
                                    # print(try_node)
                                    
                                    
        if (self.state == 'finished'):
            print("Trabajo finalizado, ruta final: ", self.getFinalRoute())
            
        if (self.state == 'waiting for nodes'):
            if (self.vecinos != []):
                self.state = 'idle'
            else:
                print("Esperando información acerca del nuevo nodo . . .")
        
        
    def runAgent(self):
        print("Tick agente: ", self.id)
        self.runSearch()
        
