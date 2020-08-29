class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find_root(self, parent, i):
        pass

    def min_spanning_tree(self):
        self.graph.sort(key=lambda item: item[2])
        nodes = []
        ranks = []

        for edge in self.graph:
            if edge[0] not in nodes:
                nodes.append(edge[0])
            if edge[1] not in nodes:
                nodes.append(edge[1])
            ranks.append(0) 

    def temp(self):
        def find_root(parent, i):
            if parent[i] == i:
                return i
            return find_root(parent, parent[i])
        
        def fusion(parent, ranks, x, y):
            xroot = find_root(parent, x)
            yroot = find_root(parent, y)

            if ranks[xroot] < ranks[yroot]:
                parent[xroot] = yroot
            elif ranks[xroot] > ranks[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                ranks[xroot] += 1
        
        self.graph.sort(key=lambda item: item[2])
        print(self.graph)

        result = []
        parent = []
        ranks = []
        for node in range(self.vertices):
            parent.append(node)
            ranks.append(0)

        e = 0
        i = 0
        while e < self.vertices - 1:
            u, v, weight = self.graph[i]
            i += 1
            x = find_root(parent, u)
            y = find_root(parent, v)

            if x != y:
                e += 1
                result.append([u, v, weight])
                fusion(parent, ranks, x, y)
            
            print("%s, %s" % (x, y))
        
        print(result)


g = Graph(7)
es = [
    ['a', 'b', 1], ['b', 'c', 7], ['c', 'd', 4],
    ['d', 'f', 5], ['f', 'g', 6], ['b', 'g', 8],
    ['c', 'g', 10], ['a', 'e', 9], ['d', 'e', 3], ['e', 'f', 2]
]

for e in es:
    g.add_edge(e[0], e[1], e[2])

# print(g.min_spanning_tree())

tg = Graph(4)
# tg.add_edge(0, 1, 10)
# tg.add_edge(0, 2, 6)
# tg.add_edge(0, 3, 5)
# tg.add_edge(1, 3, 15)
# tg.add_edge(2, 3, 4)
[tg.add_edge(edge[0], edge[1], edge[2]) for edge in es]
tg.temp()
