class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

   
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    
    def KruskalMST(self):
        result = []  
        i, e = 0, 0  
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause a cycle, include it
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree cost:", minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.KruskalMST()
