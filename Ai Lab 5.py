  tree = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F"],
    "D" : [],
    "E" : [],
    "F" : ["G"],
    "G" : []
}
Visited = list()
start = "A"
goal = "D"
def dfs(start, goal):
    if goal not in Visited:
       Visited.append(start)
       for i in tree [start]:
         dfs(i, goal)
    else:
       print("exist")
dfs(start, goal)
print(Visited)

