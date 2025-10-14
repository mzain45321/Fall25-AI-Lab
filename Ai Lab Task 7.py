class Graph:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbors(self, node):
        return self.graph[node]

    def heuristic(self, node):
        h_values = {
            "A": 1,
            "B": 1,
            "C": 1,
            "D": 1
        }
        return h_values[node]

    def a_star(self, start, goal):
        open_list = set([start])
        closed_list = set()
        g = {start: 0}
        parent = {start: None}
        while open_list:
            current = None
            for node in open_list:
                if current is None or g[node] + self.heuristic(node) < g[current] + self.heuristic(current):
                    current = node
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                print("Path found:", path)
                return path
            open_list.remove(current)
            closed_list.add(current)
            for (neighbor, cost) in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                new_cost = g[current] + cost
                if neighbor not in open_list or new_cost < g.get(neighbor, float('inf')):
                    g[neighbor] = new_cost
                    parent[neighbor] = current
                    open_list.add(neighbor)
        print("No path found!")
        return None
graph_data = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}
g = Graph(graph_data)
g.a_star('A', 'D')
