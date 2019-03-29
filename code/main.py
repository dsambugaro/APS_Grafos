#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class vertex(object):
     label = None
     value = None
     edge = []
     
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
          self.edge.append(edge)

     def remove_edge(self, edge):
          self.edge.remove(egde)

     def get_edge(self):
          edge = self.edge
          return edge

class egde(object):
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