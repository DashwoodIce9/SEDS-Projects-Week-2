class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([str(x.id) + ' : ' + str(self.connectedTo[x]) for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()
    
    def getVerticeMap(self):
        return self.vertList.values()


g=Graph()
g.addEdge('A', 'B', 7)
g.addEdge('A', 'C', 5)
g.addEdge('A', 'F', 1)
g.addEdge('B', 'A', 2)
g.addEdge('B', 'D', 7)
g.addEdge('B', 'E', 3)
g.addEdge('C', 'B', 2)
g.addEdge('C', 'F', 8)
g.addEdge('D', 'A', 1)
g.addEdge('D', 'E', 2)
g.addEdge('D', 'F', 4)
g.addEdge('E', 'A', 6)
g.addEdge('E', 'D', 5)
g.addEdge('F', 'B', 1)
g.addEdge('F', 'E', 8)

for x in g.getVerticeMap():
    print(x.__str__())
