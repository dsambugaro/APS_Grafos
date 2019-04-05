#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize

# -->>  fazer a busca em largura e adicionar os atributos de cores
# -->>  
class Vertex(object):
     label = None
     value = None
     edges = []
     
     def __init__(self,label):
          self.label = label
     
     def set_label(self, label):
          self.label = label

     def get_label(self):
          label = self.label
          return label
     
     def set_value(self, value):
          self.value = value

     def get_value(self):
          value = self.value
          return value

     def add_edge(self, edge):
          self.edges.append(edge)

     def remove_edge(self, edge):
          self.edges.remove(edge)

     def get_edges(self):
          edges = self.edges
          return edges

class Edge(object):
     label = None
     value = None
     direction= [None,None]

     def __init__(self, label):
          self.label = label

     def set_label(self, label):
          self.label = label

     def get_label(self):
          label = self.label
          return label

     def set_value(self, value):
          self.value = value

     def get_value(self):
          value = self.value
          return value

     def set_direction(self, v1, v2):
          self.direction[0] = v1
          self.direction[1] = v2
     
     def set_input(self, vertice):
          self.direction[0] = vertice
     
     def set_output(self, vertice):
          self.direction[1] = vertice

class Grafo(object):
     vertexes = []
     is_directional = False
     
     def __init__(self, is_directional):
          self.is_directional = is_directional
     
     def add_vertex(self, label, value=None):
          v = Vertex(label)
          v.set_value(value)
          self.vertexes.append(v)
     
     def remove_vertex(self, vertex):
          self.vertexes.remove(vertex)
     
     def connect_vertex(self, v1, v2, label, value=None):
          e = Edge(label)
          e.set_value(value)
          e.set_direction(v1, v2)
          v1.add_edge(e)
          v2.add_edge(e)


     def breadth_first_search(self, v_init):
          control = {
               'cor': 'branco',
               'distancia': maxsize,
               'predecessor': None
          }   
          lista = list()
          for i in len(self.vertexes): # criado para preencher a lista de controle
               lista.append(control)

          
          # for i in len(self.vertexes): # para acessar a lista de controle
          fila = list()
          fila.append(v_init)
          lista[self.vertexes.index(fila[0])]['cor'] = 'cinza'
          lista[self.vertexes.index(fila[0])]['distancia'] = 0

          while 