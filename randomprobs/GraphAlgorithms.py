'''

Graph algorithms

1. Breadth First Search
2. Depth First Search

'''

class adjNode:
    def __init__(self, data):
        self.data = data
        self.next = []

class Graph:

    def __init__(self, v):
        '''
        A graph is a list of values containing adjacence list.
        Each value has it's own adjacent elements. It means it is represented as adjacent matrix
        '''
        self.V = v # Number of vertices
        self.graph = {}


    def getOrCreate(self, node):
        if node in self.graph.keys():
            #print("While getting")
            #print(self.graph[node])
            #print(self.graph[node].next)
            return self.graph[node]
        else:
            nodeObj = adjNode(node)
            self.graph[node] = nodeObj
            return nodeObj

    def add_edge(self, node1, node2):
        '''
        :param src:
        :param des:
        :return:
        If it is an undirected graph, there has to be bidirectional connection.
        The adjacent matrix should have entry to both sides
        '''
        #print("Contect from %d to %d"%(node1,node2))
        n1 = self.getOrCreate(node1)
        n2 = self.getOrCreate(node2)
        #self.graph[node1] = adjNode(node1)
        #self.graph[node2] = adjNode(node2)
        # if Undirected graph, add edge both sides
        n1.next.append(node2)
        n2.next.append(node1)

        # if directed graph, add edge one side alone
        #n1.next.append(node2)

        #self.graph[node1].next.append(node2)
        #self.graph[node2].next.append(node1)

    def print_graph(self):

        for i in range(self.V):
            temp = self.graph[i]
            print("from %d to"%temp.data)
            for each in temp.next:
                print("%d "%self.graph[each].data, end="")
            print("\n")

    def breadth_first_search(self, graph, visited, q):
        '''
        :param graph:
        :return:
        searches in breadth manner
        '''

        if len(q) == 0:
            return
        node = q.pop(0)
        visited[node] = True

        for each in self.graph[node].next:
                if not visited[each]:
                    q.append(each)
                    print(each)
                    visited[each] = True
        self.breadth_first_search(self.graph,visited,q)

    def depth_first_search(self, graph, visited, q):
        '''
        :param graph:
        :return:
        searches in breadth manner
        '''

        if len(q) == 0:
            return
        node = q.pop(0)
        visited[node] = True

        for each in self.graph[node].next:
            if not visited[each]:
                q.append(each)
                print(each)
                visited[each] = True
                self.depth_first_search(self.graph,visited,q)


graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

#print(graph)
#for each in graph.graph.keys():
#    print(graph.graph[each].data)
#    print(graph.graph[each].next)

graph.print_graph()

visited = [False]*graph.V
q = [2]

print("Breadth First Search")
graph.breadth_first_search(graph.graph,visited,q)

visited = [False]*graph.V
q = [2]


print('Depth First Search')
graph.depth_first_search(graph.graph,visited,q)
