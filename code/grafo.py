from sys import maxsize

class Graph(object):
     graph = None
     edges_count = None
     is_directional = None

     def __init__(self, vertexes, directional=False):
          self.graph = {}
          self.edges_count = 0
          self.is_directional = directional
          self.add_vertex(vertexes)
          self.time = 0

     def __print_dict_usage(self):
          print('For dictionary entry, follow the template:')
          print("{\n\t<vertex_label>: {\n\t\t'value':<vertex_value>,\n\t\t'edges': {\n\t\t\t<edge_label>: {\n\t\t\t\t'to':<connected_vertex\'s_label>,\n\t\t\t\t'value':<edge_value>\n\t\t\t}\n\t\t}\n\t}\n}")

     def add_vertex(self, vertex_list):
          try:
               if not vertex_list:
                    return None
               if type(vertex_list) is dict:
                    unique_edges = []
                    for key, value in enumerate(vertex_list):
                         if type(value) in (int, float, str):
                              if set(('value', 'edges')) <= set(vertex_list[value]):
                                   if not vertex_list[value]['edges']:
                                        self.graph[value] = vertex_list[value]
                                   for key_edges, value_edges in enumerate(vertex_list[value]['edges']):
                                        if type(value_edges) in (int, float, str):
                                             if set(('to', 'value')) <= set(vertex_list[value]['edges'][value_edges]):
                                                  if type(vertex_list[value]['edges'][value_edges]['to']) in (int, float, str):
                                                       if vertex_list[value]['edges'][value_edges]['to'] in list(vertex_list.keys()) or vertex_list[value]['edges'][value_edges]['to'] in list(self.graph.keys()) and not self.is_directional:
                                                            for e in list(vertex_list[value]['edges'].keys()):
                                                                 if e not in unique_edges:
                                                                      unique_edges.append(e)
                                                            self.graph[value] = vertex_list[value]
                                                       else:
                                                            raise ValueError("One or more connected vertexes don't exist")
                                                  else:
                                                       raise TypeError('One or more connected vertexes have an invalid label type')
                                             else:
                                                  raise SyntaxError("One or more edges don't have the field 'to' or 'value'")
                                        else:
                                             raise TypeError('One or more edges have an invalid label type')
                              else:
                                   raise SyntaxError("One or more edges don't have the field 'to' or 'value'")
                         else:
                              raise TypeError('One or more vertexes have an invalid type as the label')
                    self.edges_count += len(unique_edges)
               else:
                    for vertex in vertex_list:
                         if type(vertex) is tuple:
                              e = {}
                              for i in range(1, len(vertex)):
                                   if type(vertex[i]) in (int, float, str):
                                        self.edges_count += 1
                                        edge_label = 'e'+str(self.edges_count)
                                        e[edge_label] = {'to': vertex[i], 'value':None}
                                        if not set(vertex[i]) <= set(self.graph):
                                             if type(vertex[i]) in (int, float, str):
                                                  if not self.is_directional:
                                                       if vertex[i] in list(self.graph.keys()):
                                                            self.graph[vertex[i]]['edges'][edge_label] = {'to': vertex[0], 'value':None}
                                                       else:
                                                            self.graph[vertex[i]] = {'value':None, 'edges': {edge_label:{'to': vertex[0], 'value':None}}}
                                                  else:
                                                       self.graph[vertex[i]] = {'value':None, 'edges': {}}
                                             else:
                                                  raise TypeError('One or more edges has an invalid type as the label')
                                   else:
                                        raise TypeError('One or more edges have an invalid label type')
                              if type(vertex[0]) in (int, float, str):
                                   if vertex[0] in list(self.graph.keys()):
                                        for edge in list(e.keys()):
                                             self.graph[vertex[0]]['edges'][edge] = e[edge]
                                   else:
                                        self.graph[vertex[0]] = {'value':None, 'edges': e}
                              else:
                                   raise TypeError('One or more edges have an invalid label type')
                         elif type(vertex) in (int, float, str):
                              self.graph[vertex] = {'value':None, 'edges':{}}
                         else:
                              raise TypeError('One or more vertexes have an invalid label type')
               return list(self.graph.keys())
          except TypeError as error:
               print("Error: ", error)
               print('Please use only integer, float or string values for labels.')
               self.__print_dict_usage()
          except ValueError as error:
               print("Error: ", error)
               print("The created Graph isn't directional. Please check your edge connections.")
               self.__print_dict_usage()
          except SyntaxError as error:
               print("Error: ", error)
               self.__print_dict_usage()

     def add_vertex_value(self, vertex, value):
          try:
               self.graph[vertex]['value'] = value
          except KeyError as error:
               print("Error: ", error)
               print("This vertex wasn't found in the Graph")

     def add_edge_value(self, edge, value):
          raise NotImplementedError('Function not yet implemented')

     def remove_vertex(self, vertex):
          try:
               v = self.graph.pop(vertex)
               for edge in v['edges']:
                    for e in self.graph[edge['to']]['edges']:
                         if e['to'] == vertex:
                              self.edges_count -= 1
                              self.graph[edge['to']]['edges'].pop(e)

          except KeyError as error:
               print("Error: ", error)
               print("This vertex wasn't found in the Graph")

     def get_vertex(self, vertex):
          try:
               v = self.graph[vertex]
               return v
          except KeyError as error:
               return None


     def get_edge(self, edge):
          raise NotImplementedError('Function not implemented')


     def connect_vertex(self, label, vertex_list, value=None):
          try:
               if len(vertex_list) > 2:
                    ValueError("One or more connected vertex don't exists")
               if set(vertex_list) <= set(self.graph):
                    for i in range(len(vertex_list)):
                         for j in range(len(vertex_list)):
                              if i != j:
                                   self.edges_count += 1
                                   self.graph[vertex_list[i]]['edges'][label]['to'] = vertex_list[j]
               else:
                    ValueError("One or more connected vertexes don't exist")
          except ValueError as error:
               print("Error: ", error)
               print("Please check your edge connections.")

     # retorna a ordem do grafo -> "bolinhas"
     def get_order(self):
          return len(list(self.graph.keys()))

     # retorna o grau de um grafo
     def get_degree(self, vertex):
          return len(self.graph[vertex]['edges'].keys())

     # retorna uma lista de todos os vertes adjacentes
     def get_neighborhood(self, vertex):
          neighborhood = []
          for e in self.graph[vertex]['edges']:
               neighborhood.append(self.graph[vertex]['edges'][e]['to'])
          return neighborhood

     # retorna todos os vertices
     def get_vertexes(self):
          return list(self.graph.keys())
     
     def is_complete(self):
          raise NotImplementedError('Function not implemented')

     # retorna true se for conexo, caso contrário retorna false
     def is_connected(self):
          vertexes = self.get_vertexes()
          vertex = [self.get_vertex(vertexes.pop(0))]
          count = 0
          next_vertexes = []

          while True:
               for v in vertex:
                    iterate = list(v['edges'].keys())
                    for e in iterate:
                         to = v['edges'][e]['to']
                         if to in vertexes:
                              next_vertexes.append(vertexes.pop(vertexes.index(to)))
               
               if next_vertexes:
                    vertex = []
                    for ve in next_vertexes:
                         vertex.append(self.get_vertex(ve))
                    next_vertexes = []
               else:
                    break

          if not vertexes:
               return True
          return False

     # retorna true se for completa, caso contrário, retorna false
     def is_complete(self):
          vertexes = self.get_vertexes()
          for vertex in vertexes:
               if self.get_degree(vertex) != self.get_order()-1:
                    return False
          return True
     
     def breadth_first_search(self, v_init, print_search_attributes=False, cicle_detection=False):
          vertexes = self.get_vertexes()
          index_init = vertexes.index(v_init)

          color = {}
          distance = {}
          predecessor = {}
          queue = []

          for vertex in vertexes:
               color[vertex] = 'white'
               distance[vertex] = maxsize
               predecessor[vertex] = []
          
          color[vertexes[index_init]] = 'grey'
          distance[vertexes[index_init]] = 0
          queue.append(vertexes[index_init])

          while queue:
               u = queue.pop(0)
               for v in self.get_neighborhood(u):
                    if color[v] == 'white':
                         color[v] = 'grey'
                         distance[v] = distance[u] + 1
                         predecessor[v].append(u)
                         queue.append(v)
                    if color[v] == 'grey' and u not in predecessor[v] and cicle_detection:
                         return True
                    color[u] = 'black'
          if print_search_attributes:
               for vertex in vertexes:
                    print('Vertex {}:\n\tColor: {}\n\tDistance: {}\n\tPredecessors: {}'.format(vertex, color[vertex], distance[vertex], predecessor[vertex]))

          if cicle_detection:
               return False

     def deep_first_search(self, print_search_attributes=False):
          def dfs_visit(u):
               self.time += 1
               distance[u]['discovery_time'] = self.time
               color[u] = 'grey'

               for v in self.get_neighborhood(u):
                    if color[v] == 'white':
                         predecessor[v].append(u)
                         dfs_visit(v)
               
               color[u] = 'black'
               self.time += 1
               distance[u]['end_time'] = self.time
          
          vertexes = self.get_vertexes()
          color = {}
          distance = {}
          predecessor = {}

          for vertex in vertexes:
               color[vertex] = 'white'
               distance[vertex] = {'discovery_time':None, 'end_time':None}
               predecessor[vertex] = []

          for vertex in vertexes:
               if color[vertex] == 'white':
                    dfs_visit(vertex)
          
          self.time = 0

          if print_search_attributes:
               for vertex in vertexes:
                    print('Vertex {}:\n\tColor: {}\n\tDistance: {}\n\tPredecessors: {}'.format(vertex, color[vertex], distance[vertex], predecessor[vertex]))

     def get_transitive_closure(self, vertex):
          vertexes = [vertex]
          reachable_vertexes = []
          visited = []
          while vertexes:
               v = vertexes.pop(0)
               visited.append(v)
               for e in list(self.graph[v]['edges']):
                    to = self.graph[v]['edges'][e]['to']
                    if to not in reachable_vertexes:
                         reachable_vertexes.append(to)

                    if to not in visited:
                         vertexes.append(to)

          return reachable_vertexes
     
     def get_inverse_transitive_closure(self, vertex):
          vertexes = self.get_vertexes()
          reachable_vertexes = []

          for v in vertexes:
               if v != vertex:
                    aux = self.get_transitive_closure(v)
                    if vertex in aux and vertex not in reachable_vertexes:
                         reachable_vertexes.append(v)

          return reachable_vertexes