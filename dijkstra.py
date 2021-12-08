'''
Dijkstra's Algorithm
is based on the principle of relaxation,
in which more accurate values gradually replace an approximation to the correct distance until the shortest distance is reached


When there are negatie weights go for bellman-ford algorithm.
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 10)
customGraph.addEdge("A", "C", 3)
customGraph.addEdge("B", "C", 2)
customGraph.addEdge("B", "D", 7)
customGraph.addEdge("B", "E", 6)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 3)
customGraph.addEdge("E", "G", 5)
customGraph.addEdge("F", "G", 1)

print(dijkstra(customGraph, "B"))
