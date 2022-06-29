'''
ID: 28390121
author: Priscilla Tham
Date: 20.05.2019
'''

class AdjNode:

    def __init__(self, item=None, link=None):
        self.item = item
        self.next = link

class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        '''
        function counts the number of items in the list
        precondition:
        :param:
        postcondition:
        :return: number of items in the list
        complexity: time: best and worst: O(1)
        '''
        return self.count

    def _get_node(self, index):
        '''
        function gets the address of the node at position index of the list
        precondition: linked list is not empty
        :param: index: position input
        postcondition:
        :return: address of the node
        complexity: time: best and worst: O(N) where N is the length of list
        error handling:
        '''
        assert 0 <= index < len(self), 'Index out of bounds.'
        node = self.head
        # when index is -1, loop runs n times
        for i in range(index):
            node = node.next
        return node

    def append(self, item):
        '''
        function appends item into array
        precondition:
        :param: item: the item to be appended into the list
        postcondition:
        :return:
        complexity: time: best: O(N) where N = 1 is possible
                          worst: O(N) where N is the length of list
        '''
        if self.head is not None:
            # when linked list is not empty, _get_index loop runs n times
            node = self._get_node(len(self) - 1)
            node.next = AdjNode(item, node.next)
        else:
            self.head = AdjNode(item, None)
        self.count += 1

class Edge:

    def __init__(self, fromVertex, toVertex, weight, toll=False):
        '''
        function creates an object of type Edge
        precondition:
        :param: fromVertex: the current vertex (current location in the road network)
                toVertex: the final vertex (destination in the road network)
                weight: the weight of the edge (road) connecting the above two vertices (travel time between the two
                locations in the road network)
                toll: a boolean indicating the existence of toll on the road along the two locations
        postcondition:
        '''
        self.location = fromVertex
        self.destination = toVertex
        self.weight = weight
        self.toll = toll


class Vertex:

    def __init__(self, id, visited=False, status=False, camera=False, service=False):
        '''
        function creates an object of type Vertex
        precondition:
        :param: id: vertex (location) identifier
                visited: a boolean indicating if the vertex (location) is visited
                status: a boolean indicating if the vertex (location) has been finalized (left the location)
                camera: a boolean indicating the existence of camera at the location
                service: a boolean indicating if the vertex (location) is a service point
        postcondition: each vertex will have a linked list storing the adjacent vertex and its corresponding weight
                       and a linked list storing the adjacent edges
        '''
        self.id = id
        self.discovered = visited
        self.finalized = status
        self.camera = camera
        self.service = service
        self.adjacentVertices = LinkedList()
        self.adjacentEdges = LinkedList()

    def addAdjacent(self, vertex, weight):
        '''
        function appends adjacent vertices and edges to corresponding linked list of the vertex
        precondition:
        :param: vertex: the adjacent vertex
                weight: the weight of the edge connecting the vertex and the adjacent vertex
        postcondition:
        :return:
        complexity: time: best and worst = O(V) where V is the total number of vertices
                    space: O(V) where V is the total number of vertices
        '''
        # when list is not empty, _get_index in append runs V times
        self.adjacentVertices.append((vertex, weight))
        edge = Edge(self, vertex, weight)
        # when list is not empty, _get_index in append runs V times
        self.adjacentEdges.append(edge)

class Graph:

    def __init__(self):
        '''
        function creates an adjacency list of graph representation
        precondition:
        :param:
        postcondition:
        '''
        self.graph = []
        self.detourGraph = []
        self.count = 0

    def __len__(self):
        '''
        function counts the number of vertices in the graph
        precondition:
        :param:
        postcondition:
        :return: number of vertices in the graph
        complexity: time: best and worst: O(1)
        error handling:
        '''
        return self.count

    def _removeDuplicates(self, data, data_size, column, list):
        '''
        function removes duplicates in a table and stores the filtered values in a list
        precondition:
        :param: data: the table containing duplicate values
                data_size: the number of items in the table
                column: table column
                list: the list for filtering the values
        postcondition:
        :return: filtered list
        complexity: time: best and worst: O(E) where E is the total number of edges
        error handling:
        '''
        # when number of edges == 1, loop runs 1 time
        # when number of edges > 1, loop runs V(V-1) times
        for j in range(data_size):
            vertex = data[j][column]
            if list[vertex] is None:
                list[vertex] = vertex

    def _open_file(self, filename):
        '''
        function opens a file in the same directory
        precondition:
        :param: filename: the name of the file containing the data of each vertices
        postcondition:
        :return: strings in file
        complexity: time: best and worst: O(1)
        error handling:
        '''
        with open(filename, 'r', encoding='UTF-8') as file:
            return file.read()

    def buildGraph(self, filename_roads):
        '''
        function fills in the adjacency list
        precondition: file containing the data of each vertices is not empty and data format is u v w in each line
                      where u is a vertex and v is the adjacent vertex and w is the weight of the edge connecting them
        :param: filename_roads: the name of the file containing the data of each vertices
        postcondition: file is not modified
        :return:
        complexity: time: best and worst: O(VE) where V is the total number of vertices and
                          E is the total number of edges
        error handling: exit function if file is not found
        '''
        try:
            # when number of edges == 1, system look for whitespace(s) once
            # when number of edges > 1, system look for whitespace(s) V(V-1) times
            content = self._open_file(filename_roads).split('\n')
            connections = len(content)
            data = []
            max = 0

            # when number of edges == 1, loop runs 1 time
            # when number of edges > 1, loop runs V(V-1) times
            for i in range(connections):
                # system looks for whitespace(s) in constant time
                values = content[i].split()
                data += [[int(values[0]), int(values[1]), float(values[2])]]
                if max < data[i][0]:
                    max = data[i][0]
                if max < data[i][1]:
                    max = data[i][1]

            vertices = [None]*(max+1)
            self._removeDuplicates(data, connections, 0, vertices)
            self._removeDuplicates(data, connections, 1, vertices)

            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            for j in range(max+1):
                vertex = Vertex(vertices[j])
                self.graph += [vertex]
                newVertex = Vertex(vertices[j])
                self.detourGraph += [newVertex]
                self.count += 1

            # when number of edges == 1, loop runs 1 time
            # when number of edges > 1, loop runs V(V-1) times
            # loop in addAdjacent runs (V-1) times
            # O(VE)
            for k in range(connections):
                self.graph[data[k][0]].addAdjacent(self.graph[data[k][1]], data[k][2])
                self.detourGraph[data[k][1]].addAdjacent(self.detourGraph[data[k][0]], data[k][2])
        except FileNotFoundError:
            return

    def augmentGraph(self, filename_camera, filename_toll):
        '''
        function identifies red-light camera identified vertices and toll identified edges
        precondition: file containing the list of red light cameras is not empty and format is u in
                      each line where u is a vertex and
                      file  containing the list of tolls is not empty and format is u v in each line
                      where u is a vertex and v is the adjacent vertex
        :param: filename_camera: the name of the file containing the containing the list of red light cameras
                filename_toll: the name of the file containing the list of tolls
        postcondition: file is not modified
        :return:
        complexity: time: best and worst: O(VE) where V is the total number of vertices and
                          E is the total number of edges
        error handling: exit function if file is not found/does not run through if graph is non-existent
        '''
        try:
            if self.count != 0:
                # when number of vertices == 1, system look for whitespace(s) once
                # when number of vertices > 1, system look for whitespace(s) V times
                cam_locations = self._open_file(filename_camera).split('\n')
                # when number of edges == 1, system look for whitespace(s) once
                # when number of edges > 1, system look for whitespace(s) V(V-1) times
                toll_roads = self._open_file(filename_toll).split('\n')

                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs V times
                for i in range(len(cam_locations)):
                    self.graph[int(cam_locations[i])].camera = True

                toll_locations = []
                # when number of edges == 1, loop runs 1 time
                # when number of edges > 1, loop runs V(V-1) times
                for j in range(len(toll_roads)):
                    # system looks for whitespace(s) in constant time
                    toll_locations += [toll_roads[j].split()]

                # when number of edges == 1, loop runs 1 time
                # when number of edges > 1, loop runs V(V-1) times
                # O(VE)
                for k in range(len(toll_locations)):
                    edges = self.graph[int(toll_locations[k][0])].adjacentEdges
                    node = edges.head
                    # when number of adjacent edges == 1, loop runs 1 time
                    # when number of adjacent edges > 1, loop runs (V-1) times
                    while node is not None:
                        if node.item.destination == self.graph[int(toll_locations[k][1])]:
                            node.item.toll = True
                        node = node.next
        except FileNotFoundError:
            return

    def addService(self, filename_service):
        '''
        function identifies service point identified vertices
        precondition: file containing the list of service locations is not empty and format is u in
                      each line where u is a vertex and
        :param: filename_service: the name of the file containing the list of service locations
        postcondition: file is not modified
        :return:
        complexity: time: best and worst: O(V) where V is the total number of vertices
        error handling: exit function if file is not found/does not run through if graph is non-existent
        '''
        try:
            if self.count != 0:
                # when number of vertices == 1, system look for whitespace(s) once
                # when number of vertices > 1, system look for whitespace(s) V times
                servicePoints = self._open_file(filename_service).split('\n')

                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs V times
                for i in range(len(servicePoints)):
                    self.graph[int(servicePoints[i])].service = True
                    self.detourGraph[int(servicePoints[i])].service = True
        except FileNotFoundError:
            return

    def _rise(self, heapList):
        '''
        function moves item up the heap accordingly
        precondition:
        :param: heapList: the heap array
        postcondition: heap array is stable
        :return:
        complexity: time: best and worst: O(log V) where V is the size of the heap
        error handling:
        '''
        n = len(heapList)-1
        # loop runs log V time(s)
        while n > 1 and heapList[n // 2][1] > heapList[n][1]:
            heapList[n // 2], heapList[n] = heapList[n], heapList[n // 2]
            n //= 2

    def _sink(self, heapList):
        '''
        function moves item down the heap accordingly
        precondition:
        :param: heapList: the heap array
        postcondition: heap array is stable
        :return:
        complexity: time: best and worst: O(log V) where V is the size of the heap
        error handling:
        '''
        root = 1
        # loop runs log V time(s)
        while 2 * root <= len(heapList) - 1:
            child = 2 * root
            if child + 1 < len(heapList) and heapList[child + 1][1] < heapList[child][1]:
                child += 1
            if heapList[root][1] > heapList[child][1]:
                heapList[root], heapList[child] = heapList[child], heapList[root]
            else:
                return
            root = child

    def calculatePath(self, graph, list, source, target):
        '''
        function retrieves vertices in the order of the quickest path from the source to the target and
        the time taken to reach the target from the source
        precondition: list is not empty and list contains source and target
        :param: graph: adjacency list
                list: list of visited vertices (locations left)
                source: positive integer indicating the vertex id of the source
                target: positive integer indicating the vertex id of the target
        postcondition: adjacency list representing the graph (self.graph) is not modified
        :return:
        complexity: time: best and worst: O(V) where V is the total number of vertices
        error handling:
        '''
        path = []
        time = -1
        current = graph[target]
        i = len(list) - 1
        # when number of vertices == 1, loop runs 1 time
        # when number of vertices > 1, loop runs V times
        while i >= 0:
            if list[i][0] == current:
                path += [current.id]
                if current.id == target:
                    time = list[i][1]
                if current != graph[source]:
                    current = list[i][2]
                    i = len(list) - 1
            i -= 1
        # list slicing cost V
        result = (path[::-1], time)
        return result

    def quickestPath(self, source, target):
        '''
        function finds the path with the least travel time from a location to a destination
        precondition:
        :param: source: location
                target: destination
        postcondition: adjacency list representing the graph (self.graph) is not modified
        :return: 2 values within a tuple a) list containing all locations in the order of the quickest path traversal
                from the source to the target and b) total time required to reach the source from the target
        complexity: time: best: O(V) where V is the total number of vertices
                          worst: O(E log V) where V is the total number of vertices and E is the total number of edges
        error handling: does not run through if graph is non-existent
        '''
        if self.count != 0:
            discoveredHeap = [None]
            finalized = []
            lookup = [-1]*self.count

            target = int(target)
            source = int(source)
            self.graph[source].discovered = True
            discoveredHeap += [[self.graph[source], 0]]

            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            while len(discoveredHeap) != 1:
                current = discoveredHeap[1]
                # system looks for item in constant time
                discoveredHeap.remove(current)
                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs (log V) times
                self._sink(discoveredHeap)

                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs V times
                for i in range(1, len(discoveredHeap)):
                    lookup[discoveredHeap[i][0].id] = i

                neighbours = current[0].adjacentVertices
                if len(neighbours) != 0:
                    node = neighbours.head
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs (V-1) times
                    # best case when source is the target
                    while node is not None:
                        weight = node.item[1] + current[1]
                        if not node.item[0].discovered and not node.item[0].finalized:
                            node.item[0].discovered = True
                            discoveredHeap += [[node.item[0], weight, current[0]]]
                            # when number of vertices == 1, loop runs 1 time
                            # when number of vertices > 1, loop runs (log V) times
                            self._rise(discoveredHeap)
                        elif not node.item[0].finalized:
                            index = lookup[node.item[0].id]
                            if index != -1 and discoveredHeap[index][1] > weight:
                                discoveredHeap[index][1] = weight
                                discoveredHeap[index][2] = current[0]
                                # when number of vertices == 1, loop runs 1 time
                                # when number of vertices > 1, loop runs (log V) times
                                self._rise(discoveredHeap)
                        node = node.next
                    current[0].finalized = True
                    finalized += [current]
                    lookup[current[0].id] = -2

                if current[0] == self.graph[target]:
                    if finalized[-1][0].id != target:
                        finalized += [current]
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs V times
                    return self.calculatePath(self.graph, finalized, source, target)
        return [[], -1]

    def quickestSafePath(self, source, target):
        '''
        function finds the safest path with the least travel time from a location to a destination
        precondition:
        :param: source: location
                target: destination
        postcondition: adjacency list representing the graph (self.graph) is not modified
        :return: 2 values within a tuple a) list containing all locations in the order of the quickest safe path
                traversal from the source to the target and b) total time required to reach the source from the target
                along the safe path
        complexity: time: best: O(V) where V is the total number of vertices
                          worst: O(E log V) where V is the total number of vertices and E is the total number of edges
        error handling: does not run through if graph is non-existent
        '''
        if self.count != 0:
            discoveredHeap = [None]
            finalized = []
            lookup = [-1] * self.count

            target = int(target)
            source = int(source)
            self.graph[source].discovered = True
            discoveredHeap += [[self.graph[source], 0]]

            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            while len(discoveredHeap) != 1 and not self.graph[source].camera:
                current = discoveredHeap[1]
                # system looks for item in constant time
                discoveredHeap.remove(current)
                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs (log V) times
                self._sink(discoveredHeap)

                # when number of vertices == 1, loop runs 1 time
                # when number of vertices > 1, loop runs V times
                for i in range(1, len(discoveredHeap)):
                    lookup[discoveredHeap[i][0].id] = i

                neighbours = current[0].adjacentEdges
                if len(neighbours) != 0:
                    node = neighbours.head
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs (V-1) times
                    # best case when source is the target
                    while node is not None:
                        weight = node.item.weight + current[1]
                        if not node.item.destination.discovered and not node.item.destination.finalized and \
                                not node.item.destination.camera and not node.item.toll:
                            node.item.destination.discovered = True
                            discoveredHeap += [[node.item.destination, weight, current[0]]]
                            # when number of vertices == 1, loop runs 1 time
                            # when number of vertices > 1, loop runs (log V) times
                            self._rise(discoveredHeap)
                        elif not node.item.destination.finalized:
                            index = lookup[node.item.destination.id]
                            if index != -1 and discoveredHeap[index][1] > weight:
                                discoveredHeap[index][1] = weight
                                discoveredHeap[index][2] = current[0]
                                # when number of vertices == 1, loop runs 1 time
                                # when number of vertices > 1, loop runs (log V) times
                                self._rise(discoveredHeap)
                        node = node.next
                    current[0].finalized = True
                    finalized += [current]
                    lookup[current[0].id] = -2

                if current[0] == self.graph[target] and not current[0].camera:
                    if finalized[-1][0].id != target:
                        finalized += [current]
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs V times
                    return self.calculatePath(self.graph, finalized, source, target)
        return [[], -1]

    def dijkstra(self, graph, source):
        '''
        function finds the minimum time to travel from a location to all other locations
        precondition:
        :param: graph: adjacency list
                source: location
        postcondition: adjacency list representing the graph (self.graph) is not modified
        :return: list containing all locations in the order of the quickest path
                traversal from the source to all
        complexity: time: best and worst: O(E log V) where V is the total number of vertices and
                          E is the total number of edges
        error handling:
        '''
        discoveredHeap = [None]
        finalized = []
        lookup = [-1]*self.count

        graph[source].discovered = True
        discoveredHeap += [[graph[source], 0]]

        # when number of vertices == 1, loop runs 1 time
        # when number of vertices > 1, loop runs V times
        while len(discoveredHeap) != 1:
            current = discoveredHeap[1]
            # system looks for item in constant time
            discoveredHeap.remove(current)
            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs (log V) times
            self._sink(discoveredHeap)

            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            for i in range(1, len(discoveredHeap)):
                lookup[discoveredHeap[i][0].id] = i

            neighbours = current[0].adjacentVertices
            node = neighbours.head
            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs (V-1) times
            while node is not None:
                weight = node.item[1] + current[1]
                if not node.item[0].discovered and not node.item[0].finalized:
                    node.item[0].discovered = True
                    discoveredHeap += [[node.item[0], weight, current[0]]]
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs (log V) times
                    self._rise(discoveredHeap)
                elif not node.item[0].finalized:
                    index = lookup[node.item[0].id]
                    if index != -1 and discoveredHeap[index][1] > weight:
                        discoveredHeap[index][1] = weight
                        discoveredHeap[index][2] = current[0]
                        # when number of vertices == 1, loop runs 1 time
                        # when number of vertices > 1, loop runs (log V) times
                        self._rise(discoveredHeap)
                node = node.next
            current[0].finalized = True
            finalized += [current]
            lookup[current[0].id] = -2
        return finalized

    def quickestDetourPath(self, source, target):
        '''
        function finds the path with the least travel time from a location to a destination passing through at least
        one of the service point
        precondition:
        :param: source: location
                target: destination
        postcondition: adjacency list representing the graph (self.graph/self.detourGraph) is not modified
        :return: 2 values within a tuple a) list containing all locations in the order of the quickest path traversal
                from the source to the target and b) total time required to reach the source from the target along the
                quickest detour path
        complexity: time: best and worst: O(E log V) where V is the total number of vertices and
                          E is the total number of edges
        error handling: does not run through if graph is non-existent
        '''
        if self.count != 0:
            target = int(target)
            source = int(source)
            finalized = self.dijkstra(self.graph, source)
            reversedFinalized = self.dijkstra(self.detourGraph, target)

            reachable = []
            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            for j in range(len(reversedFinalized)):
                if reversedFinalized[j][0].service:
                    reachable += [reversedFinalized[j]]

            finalizedPath = None
            time = float('inf')
            # when number of vertices == 1, loop runs 1 time
            # when number of vertices > 1, loop runs V times
            for k in range(len(reachable)):
                fstHalf = self.calculatePath(self.graph, finalized, source, reachable[k][0].id)
                sndHalf = self.calculatePath(self.detourGraph, reversedFinalized, target, reachable[k][0].id)
                timeTaken = fstHalf[1]+sndHalf[1]
                if len(fstHalf[0]) != 0 and time > timeTaken:
                    path = []
                    path += fstHalf[0]
                    # when number of vertices == 1, loop runs 1 time
                    # when number of vertices > 1, loop runs V times
                    for m in range(len(sndHalf[0])-2, -1, -1):
                        path += [sndHalf[0][m]]
                    finalizedPath = path
                    time = timeTaken

            if finalizedPath is not None:
                result = (finalizedPath, time)
                return result
        return [[], -1]

if __name__ == '__main__':
    graph = Graph()
    graph.buildGraph('basicGraph.txt')
    # print(graph)
    # print(graph.quickestPath(31, 0))
    graph.augmentGraph('cameraljskd.txt', 'toll.txt')
    # print(graph.quickestSafePath(20, 29))
    graph.addService('service.txt')
    print(graph.quickestDetourPath(20, 29))

