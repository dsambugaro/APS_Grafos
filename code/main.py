#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from grafo import Graph

def main():
     graph = {
          'a':{'value':None, 'edges':{'e1':{'to':'b','value':None}, 'e5':{'to':'c','value':None}}},
          'b':{'value':None, 'edges':{'e1':{'to':'a','value':None},'e4':{'to':'c','value':None}}},
          'c':{'value':None, 'edges':{'e5':{'to':'a','value':None}}}
     }
     G = Graph(graph)
     print("\n\n")
     print("Graph:\n")
     for x in G.graph:
          print (x)
          for y in G.graph[x]:
               print (y,':',G.graph[x][y])
     print("\n==========================================\n")
     vertexes = G.get_vertexes()
     print("Vertexes: ", vertexes)
     print("Degree of vertex {}: ".format(vertexes[0]), G.get_degree(vertexes[0]))
     print("Neighborhood of vertex {}: ".format(vertexes[0]), G.get_neighborhood(vertexes[0]))
     print("Edges count: ", G.edges_count)
     print("Order: ", G.get_order())
     print("is_connected: ", G.is_connected())
     print("is_complete: ", G.is_complete())

if __name__ == '__main__':
     main()