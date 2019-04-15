#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize

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

class Graph(object):
     graph = {}
     vertexes = []
     edges = []
     is_directional = False
     
     def __init__(self, vertexes):
          self.vertexes = vertexes
     
     def add_vertex(self, label, value=None):
          v = Vertex(label)
          v.set_value(value)
          self.vertexes.append(v)

     def remove_vertex(self, vertex):
          self.vertexes.remove(vertex)
     
     def find_vertex(self, value, search_type='label', answer_type='index'):
          occurrences = []
          try:
               for i in range(len(self.vertexes)):
                    if search_type == 'label':
                         if self.vertexes[i].get_label() == value:
                              if answer_type == 'index':
                                   occurrences.append(i)
                              elif answer_type == 'obj':
                                   occurrences.append(self.vertexes[i])
                              else:
                                   raise Exception('Invalid answer type')
                    elif search_type == 'value':
                         if self.vertexes[i].get_value() == value:
                              if answer_type == 'index':
                                   occurrences.append(i)
                              elif answer_type == 'obj':
                                   occurrences.append(self.vertexes[i])
                              else:
                                   raise Exception('Invalid answer type')
                    else:
                         raise Exception('Invalid search type')
               return occurrences
          except Exception as e:
               print('An Error has occured.')
               print(e)
     
     def find_edge(self, value, search_type='label', answer_type='index'):
          occurrences = []
          try:
               for i in range(len(self.vertexes)):
                    if search_type == 'label':
                         if self.edges[i].get_label() == value:
                              if answer_type == 'index':
                                   occurrences.append(i)
                              elif answer_type == 'obj':
                                   occurrences.append(self.edges[i])
                              else:
                                   raise Exception('Invalid answer type')
                    elif search_type == 'value':
                         if self.edges[i].get_value() == value:
                              if answer_type == 'index':
                                   occurrences.append(i)
                              elif answer_type == 'obj':
                                   occurrences.append(self.edges[i])
                              else:
                                   raise Exception('Invalid answer type')
                    else:
                         raise Exception('Invalid search type')
               return occurrences
          except Exception as e:
               print('An Error has occured.')
               print(e)

     def connect_vertex(self, label, v1, v2):
          e = Edge(label)
          e.set_direction(v1, v2)
          v1.add_edge(e)
          v2.add_edge(e)
          self.edges.append(e)


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