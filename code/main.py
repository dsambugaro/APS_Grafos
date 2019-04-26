#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from grafo import Graph

def main():
     graph_example = [('s','r','w'),('r','v'),('w','t','x'),('t','x','u'), ('x','y'),('u','y')]
     G = Graph(graph_example)
     print("\n\n")
     print("Graph:\n")
     for x in G.graph:
          print ('Vertex: ',x)
          for y in G.graph[x]:
               print ('\t', y,':',G.graph[x][y])
     print("\n==========================================\n")
     vertexes = G.get_vertexes()
     print("Vertexes: ", vertexes)
     print("Degree of vertex {}: ".format(vertexes[0]), G.get_degree(vertexes[0]))
     print("Neighborhood of vertex {}: ".format(vertexes[0]), G.get_neighborhood(vertexes[0]))
     print("Edges count: ", G.edges_count)
     print("Order: ", G.get_order())
     print("is_connected: ", G.is_connected())
     print("is_complete: ", G.is_complete())
     
     print('\n\n')
     
     print('Breadth First Search: ')
     G.breadth_first_search('s',print_search_attributes=True)
     
     print('\n\n')

     print('Deep First Search: ')
     G.deep_first_search(print_search_attributes=True)
     
     print('\n\n')

     print('Transitive Closure: {}'.format(G.get_transitive_closure(vertexes[0])))
     print('Inverse Transitive Closure: {}'.format(G.get_inverse_transitive_closure(vertexes[0])))

if __name__ == '__main__':
     main()