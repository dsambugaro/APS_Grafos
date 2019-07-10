from sys import maxsize


class Graph(object):
    graph = None
    edges_count = None
    is_directional = None

    def __init__(self, vertexes=None, is_directional=False):
        self.graph = {}
        self.edges_count = 0
        self.is_directional = is_directional
        if vertexes:
            self.add_vertex(vertexes)
        self.time = 0

    def add_vertex(self, vertex_list):
        if not vertex_list:
            return None
        for vertex in vertex_list:
            if type(vertex) is tuple:
                e = {}
                for i in range(1, len(vertex)):
                    self.edges_count += 1
                    edge_label = 'e'+str(self.edges_count)
                    e[edge_label] = {'to': vertex[i], 'value': None}
                    if not set(vertex[i]) <= set(self.graph):
                        if not self.is_directional:
                            if vertex[i] in list(self.graph.keys()):
                                self.graph[vertex[i]]['edges'][edge_label] = {
                                    'to': vertex[0], 'value': None}
                            else:
                                self.graph[vertex[i]] = {'value': None, 'edges': {
                                    edge_label: {'to': vertex[0], 'value': None}}}
                        else:
                            if vertex[i] not in list(self.graph.keys()):
                                self.graph[vertex[i]] = {
                                    'value': None, 'edges': {}}
                    if vertex[0] in list(self.graph.keys()):
                        for edge in list(e.keys()):
                            if not self.has_edge_to(vertex[0], e[edge]['to']):
                                self.graph[vertex[0]]['edges'][edge] = e[edge]
                    else:
                        self.graph[vertex[0]] = {'value': None, 'edges': e}
            else:
                self.graph[vertex] = {'value': None, 'edges': {}}
        return list(self.graph.keys())

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

    def has_edge_to(self, from_v, to_v):
        for edge in list(self.graph[from_v]['edges'].keys()):
            if self.graph[from_v]['edges'][edge]['to'] == to_v:
                return True
        return False

    def connect_vertex(self, vertex_list, label=None, value=None):
        self.edges_count += 1
        if not label:
            edge_label = 'e'+str(self.edges_count)
        else:
            edge_label = label

        self.graph[vertex_list[0]]['edges'][edge_label]['to'] = vertex_list[1]
        if not self.is_directional:
            self.graph[vertex_list[1]
                    ]['edges'][edge_label]['to'] = vertex_list[0]

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
        if not vertexes:
            return False
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

    def breadth_first_search(self, v_init, v_target=None, print_search_attributes=False, cicle_detection=False):
        vertexes = self.get_vertexes()
        if not v_init in vertexes:
            return -1
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
                if v_target and v == v_target:
                    return distance[v]
                if color[v] == 'grey' and u not in predecessor[v] and cicle_detection:
                    return True
                color[u] = 'black'
        if print_search_attributes:
            for vertex in vertexes:
                print('Vertex {}:\n\tColor: {}\n\tDistance: {}\n\tPredecessors: {}'.format(
                    vertex, color[vertex], distance[vertex], predecessor[vertex]))

        if cicle_detection:
            return False
        return -1

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
            distance[vertex] = {'discovery_time': None, 'end_time': None}
            predecessor[vertex] = []

        for vertex in vertexes:
            if color[vertex] == 'white':
                dfs_visit(vertex)

        self.time = 0

        if print_search_attributes:
            for vertex in vertexes:
                print('Vertex {}:\n\tColor: {}\n\tDistance: {}\n\tPredecessors: {}'.format(
                    vertex, color[vertex], distance[vertex], predecessor[vertex]))

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
