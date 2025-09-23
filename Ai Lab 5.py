# def fibon(n=10):
#    fib = []
#    num1 = 0
#    num2 = 1
#    if n == 0:
#       return fib
#    elif n == 1:
#       return num1
#    elif n == 1:
#       return num2
#    else:
#       fibs = fibon(n-1)
#       fibs.append


  
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
