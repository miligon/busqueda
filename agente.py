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
        self.posicion_actual = [0, 0]  # ruta, profundidad
        self.cambios_de_ruta = [[],[]]
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
        self.setPos([0, 0])

    def setFinal(self, final):
        print("Ciudad final:", final)
        self.final = final

    def setBehavior(self, modo):
        if (modo == 'amplitud'):
            self.modoBusqueda = 'amplitud'
        else:
            self.modoBusqueda = 'profundidad'

    def setPos(self, pos):
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

    def move(self, destino):
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
        else:
            if(pos[1] > 0):
                if (destino == self.ruta[pos[0]][pos[1]-1]):
                    # Up
                    new_pos = [pos[0], (pos[1] - 1)]
                    self.setPos(new_pos)
                    return True
        return False

    def moveTo(self, destino):
        print("moviendo a: ", destino)
        if (destino not in self.vecinos and
                destino not in self.ruta[self.posicion_actual[0]]):
            # Cambio de rama, buscar el nodo que tiene como vecino a destino
            while (destino not in self.vecinos):
                time.sleep(0.1)
                if (self.posicion_actual[1] > 0):
                    new_depth = self.posicion_actual[1]-1
                    key = self.ruta[self.posicion_actual[0]][new_depth]
                    print("regresando a:", key)
                    self.move(key)
                else:
                    print("Llegue a inicio sin encontrar la rama")
                    return False
                
                if (destino not in self.vecinos):
                    for route in self.ruta:
                        depth_i = self.posicion_actual[1]
                        key = self.ruta[self.posicion_actual[0]][depth_i]
                        #print("key: - ", key, "destino: ", destino, route)
                        if (key == route[depth_i] and destino in route[depth_i+1:]):
                            print("if: ", destino, route[depth_i+1:])
                            print("Cambiando a ruta existente")
                            route_num = self.ruta.index(route)
                            self.posicion_actual[0]=route_num
                            self.moveTo(destino)
                            return

            if (destino in self.vecinos):
                print("CAMBIANDO A NUEVA RUTA :D")
                depth_i = self.posicion_actual[1] + 1
                route = self.posicion_actual[0]
                
                nueva_ruta = self.ruta[route][:depth_i]
                self.ruta.append(nueva_ruta)
                self.posicion_actual[0] = route + 1
                pos = [route,(depth_i-1)]
                print("pos:", pos)
                if (pos in self.cambios_de_ruta[0]):
                    i_rutas = self.cambios_de_ruta[0].index(pos)
                    print("a: ", pos, i_rutas)
                    self.cambios_de_ruta[1][i_rutas].append([route+1])
                else:
                    self.cambios_de_ruta[0].append(pos)
                    self.cambios_de_ruta[1].append([route, route+1])
                    
                self.move(destino)

        else:
            if (destino in self.vecinos):
                self.move(destino)
            else:
                if (destino in self.ruta[self.posicion_actual[0]]):
                    # Descender en una ruta en la que se encuentra el destino
                    while (destino not in self.vecinos):
                        time.sleep(0.1)
                        if (self.posicion_actual[1] < (len(self.ruta[self.posicion_actual[0]])-1)):
                            new_depth = self.posicion_actual[1]+1
                            key = self.ruta[self.posicion_actual[0]][new_depth]
                            print("avanzando a:", key)
                            self.move(key)
                        else:
                            print("Llegue a inicio sin encontrar la rama")
                            return False
                    self.move(destino)

    def runSearch(self):
        self.buffer_busqueda = self.vecinos.copy()
        
        
        while(len(self.buffer_busqueda) > 0):
            try_node = self.buffer_busqueda.pop()
            self.moveTo(try_node)
            time.sleep(0.1)
            if (self.final == try_node):
                print("ENCONTRE:", try_node)
                return self.ruta[self.posicion_actual[0]]

            nodes = self.vecinos.copy()
            if len(nodes) != 0:
                for child in nodes:
                    if (child not in self.visitados):
                        if (self.modoBusqueda == 'amplitud'):
                            self.buffer_busqueda.insert(0, child)
                        else:
                            self.buffer_busqueda.append(child)
                            # print(try_node)
