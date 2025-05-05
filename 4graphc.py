class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, color, v, c):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True

    def graph_color_util(self, m, color, v):
        if v == self.V:
            return True
        for i in range(1, m + 1):
            if self.is_safe(color, v, i):
                color[v] = i
                if self.graph_color_util(m, color, v + 1):
                    return True
                color[v] = 0
        return False

    def graph_color(self, m):
        color = [0] * self.V
        if self.graph_color_util(m, color, 0):
            color_names = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Pink", "Brown"]
            if m > len(color_names):
                print("Not enough color names provided for this value of m.")
                return False

            print("\nVertex coloring:")
            for i in range(self.V):
                print("Vertex", i, "->  Color: ", color_names[color[i] - 1])
            return True

        print("Solution does not exist")
        return False


V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter the edges:")
for i in range(E):
    print("Edge ", i + 1, " : ")
    u = int(input("  Enter first vertex: "))
    v = int(input("  Enter second vertex: "))
    g.add_edge(u, v)


m = int(input("Enter number of colors: "))
g.graph_color(m)

