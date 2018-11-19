from collections import defaultdict
# define a class Tree, which contains 3 items:
# 1. value - type Any
# 2. left subtree - type Tree
# 3. right subtree - type Tree


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order(root):
    result = []
    if root:
        result += in_order(root.left)
        result.append(root.value)
        result += in_order(root.right)
    return result


# Preorder traversal
def pre_order(root):
    result = []
    if root:
        result.append(root.value)
        result += pre_order(root.left)
        result += pre_order(root.right)
    return result


def post_order(root):
    result = []
    if root:
        result += post_order(root.left)
        result += post_order(root.right)
        result.append(root.value)
    return result


g = Tree('G')
j = Tree('J')
k = Tree('K')
l = Tree('L')
f = Tree('F')
h = Tree('H', left=j)
i = Tree('I', left=k, right=l)
e = Tree('E', right=i)
c = Tree('C', e, f)
d = Tree('D', g, h)
b = Tree('B', right=d)
a = Tree('A', b, c)
print(in_order(a))
print(pre_order(a))
print(post_order(a))

# Class to represent a graph


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # list of edges (u, v, w)

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # The main function to construct MST using Kruskal's algorithm

    def mst(self):
        self.graph.sort(key=lambda item: item[2])
        result = []
        trim0 = []
        trim1 = []

        for i in range(len(self.graph)):
            if len(result) < 2 or (len(result) < self.V and self.graph[i][0] not in trim0 and self.graph[i][1] not in trim1):
                trim0.append(self.graph[i][0])
                trim1.append(self.graph[i][1])
                result.append(self.graph[i])
        return result

class DGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])
    def find_root(self, roots, node):
        """find chosen node's root"""
        if roots[node] == node:
            return node
        return self.find_root(roots, roots[node])

    def fusion(self, roots, ranks, node1, node2):
        """fusion by rank 2 sets under the chosen root"""
        node1_root = self.find_root(roots, node1)
        node2_root = self.find_root(roots, node2)

        if ranks[node1_root] < ranks[node2_root]:
            roots[node1_root] = node2_root
        elif ranks[node1_root] > ranks[node2_root]:
            roots[node2_root] = node1_root
        else:
            roots[node1_root] = node2_root
            ranks[node2_root] += 1

    def min_spanning_tree(self):
        self.graph.sort(key=lambda item: item[2])
        result = []

        roots = {}
        ranks = []
        node_i = 0
        for i in range(self.vertices):
            if self.graph[i][0] not in roots:
                roots[node_i] = self.graph[i][0]
                node_i += 1
            if self.graph[i][1] not in roots:
                roots[node_i] = self.graph[i][1]
                node_i += 1
            ranks.append(0)

        edge = 0
        index = 0
        while edge < self.vertices - 1:
            u, v, weight = self.graph[index]
            index += 1
            u_root = self.find_root(roots, u)
            v_root = self.find_root(roots, v)
            
            if u_root != v_root:
                edge += 1
                result.append([u, v, weight]) 
                self.fusion(roots, ranks, u_root, v_root)
        
        return result


g = Graph(7)
es = [
    ['a', 'b', 1], ['b', 'c', 7], ['c', 'd', 4],
    ['d', 'f', 5], ['f', 'g', 6], ['b', 'g', 8],
    ['c', 'g', 10], ['a', 'e', 9], ['d', 'e', 3], ['e', 'f', 2]
]

for e in es:
    g.add_edge(e[0], e[1], e[2])

# print(g.min_spanning_tree())
print(g.mst())

g1 = Graph(8)
es1 = [
    ['v0', 'v1', 12], ['v1', 'v2', 20], ['v2', 'v7', 19], ['v1', 'v3', 5],
    ['v3', 'v7', 18], ['v1', 'v4', 7], ['v3', 'v4', 2], ['v4', 'v7', 15],
    ['v6', 'v7', 13], ['v5', 'v6', 8], ['v4', 'v5', 10], ['v0', 'v5', 4]
]

for e in es1:
    g1.add_edge(e[0], e[1], e[2])

print(g1.mst())
