# Task 1

graph = {
   'A':['B','C'],
   'B':['D','E'],
   'C':['F'],
   'D':['G','H'],
   'E':[],
   'F':['I','K'],
   'G':[],
   'H':['L'],
   'I':[],
   'K':['M'],
   'L':[],
   'M':[]
}
def BFS(start, goal):
    visited = []
    level = [start]
    while level:
        ne_xt = []
        for n in level:
            if n not in visited:
                
                visited.append(n)
                if n == goal:
                    
                    return visited
                ne_xt.extend(graph[n])
                     
                for c in graph[n]:
                    ne_xt.append(c)
        level = ne_xt
    print ("Not Found")
    return visited
result = BFS("A", "M")
print(result)


# Task 2

def bfs(graph, start, goal):
    traversed = []
    q = [start]

    while q:
        current = q.pop(0)

        if current not in traversed:
            traversed.append(current)

            if current == goal:
                print("Target Found")
                return traversed

            q.extend(graph[current])

    print("Target Not Found")
    return traversed


graph_data = {
   'A':['B','C'],
   'B':['D','E'],
   'C':['F'],
   'D':['G','H'],
   'E':[],
   'F':['I','K'],
   'G':[],
   'H':['L'],
   'I':[],
   'K':['M'],
   'L':[],
   'M':[]
}
result = bfs(graph_data, "A", "G")
print("sequence:", result)
