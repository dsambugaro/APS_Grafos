#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize

class Graph(object):
     graph = None
     edges_count = None
     is_directional = False

     def __init__(self, vertexes):
          self.graph = {}
          self.edges_count = 0
          self.add_vertex(vertexes)

     def __print_dict_usage(self):
          print('For dictionary entry, follow the template:')
          print("[{\n\t<vertex_label>: {\n\t\t'value':<vertex_value>,\n\t\t'edges': {\n\t\t\t<edge_label>: {\n\t\t\t\t'to':<connected_vertex\'s_label>,\n\t\t\t\t'value':<edge_value>\n\t\t\t}\n\t\t}\n\t}\n}"])

     def add_vertex(self, vertex_list):
          try:
               if type(vertex_list) in (dict):
                         for key, value in enumerate(vertex_list):
                              if type(value in (int, float, str)):
                                   if set(('value', 'edges')) <= set(vertex_list[value]):
                                        for key_edges, value_edges in vertex_list[value]['edges']:
                                             if type(value_edges in (int, float, str)):
                                                  if set(('to', 'value')) <= set(vertex_list[value_edges]):
                                                       if type(vertex_list[value_edges]['to']) in (int, float, str):
                                                            if vertex_list[value_edges]['to'] in list(vertex_list.keys()) or vertex_list[value_edges]['to'] in list(self.graph.keys()) and not self.is_directional:
                                                                 self.graph[value] = vertex_list[value]
                                                            else:
                                                                 raise ValueError("One or more connected vertex don't exists")
                                                       else:
                                                            raise TypeError('One or more connected vertex has an invalid type as the label')
                                                  else:
                                                       raise SyntaxError("One or more edges don't have the fields 'to' or 'value'")
                                             else:
                                                  raise TypeError('One or more edge has an invalid type as the label')
                                   else:
                                        raise SyntaxError("One or more edges don't have the fields 'to' or 'value'")
                              else:
                                   raise TypeError('One or more vertex has an invalid type as the label')
               else:
                    for vertex in vertex_list:
                         if type(vertex) is tuple:
                              e = {}
                              for i in range(1, len(vertex)):
                                   if type(vertex[i]) in (int, float, str):
                                        self.edges_count += 1
                                        e['e'+str(self.edges_count)] = {'to': vertex[i], 'value':None}
                                   else:
                                        raise TypeError('One or more edges has an invalid type as the label')
                              if type(vertex[0]) in (int, float, str):
                                   graph[vertex[0]] = {'value':None, 'edges': e}
                              else:
                                   raise TypeError('One or more edges has an invalid type as the label')
                         elif type(vertex) in (int, float, str):
                              self.graph[vertex] = {'value':None, 'edges':{}}
                         else:
                              raise TypeError('One or more vertex has an invalid type as the label')
          except TypeError as error:
               print("Error:", error)
               print('Please use only integer, float or string values for labels.')
               self.__print_dict_usage()
          except ValueError as error:
               print("Error:", error)
               print("The created Graph isn't directional. Please check your edges connections.")
               self.__print_dict_usage()
          except SyntaxError as error:
               print("Error:", error)
               self.__print_dict_usage()

     def add_vertex_value(self, vertex, value):
          try:
               self.graph[vertex]['value'] = value
          except KeyError as error:
               print("Error:", error)
               print("This vertex wasn't found in the Graph")

     def add_edge_value(self, edge, value):
          raise NotImplementedError('Function not implemented')

     def remove_vertex(self, vertex):
          try:
               v = self.graph.pop(vertex)
               for edge in v['edges']:
                    for e in self.graph[edge['to']]['edges']:
                         if e['to'] == vertex:
                              self.edges_count -= 1
                              self.graph[edge['to']]['edges'].pop(e)

          except KeyError as error:
               print("Error:", error)
               print("This vertex wasn't found in the Graph")

     def find_vertex(self, vertex):
          try:
               v = self.graph[vertex]
               return v
          except KeyError as error:
               return None

     def find_edge(self, edge):
          raise NotImplementedError('Function not implemented')

     def connect_vertex(self, label, vertex_list, value=None):
          try:
               if set(vertex_list) <= set(self.graph):
                    for i in range(len(vertex_list)):
                         for j in range(len(vertex_list)):
                              if i != j:
                                   self.edges_count += 1
                                   self.graph[vertex_list[i]]['edges'][label]['to'] = vertex_list[j]
               else:
                    ValueError("One or more connected vertex don't exists")
          except ValueError as error:
               print("Error:", error)
               print("Please check your edges connections.")

     def breadth_first_search(self, v_init):
          control = {
               'cor': 'branco',
               'distancia': maxsize,
               'predecessor': None
          }   
          lista = {}
          for key, value in enumerate(self.graph):
               lista[value] = control

          fila = []
          fila.append(v_init)
          lista[fila[0]]['cor'] = 'cinza'
          lista[fila[0]]['distancia'] = 0

          # while 