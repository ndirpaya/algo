
def add_point(point):
    if point not in graph:
        graph[point] = []

def add_road(point1, point2):
    if point1 and point2 in graph:
        graph[point1].append(point2)
        graph[point2].append(point1)
    else:
        return

def add_road_paced(point1, point2, pace):
    if point1 and point2 in graph:
        list1 = [point2, pace]
        list2 = [point1, pace]
        graph[point1].append(list1)
        graph[point2].append(list2)
    else:
        return

def DFS(point, visited, graph):
    if point not in graph:
        return
    if point not in visited:
        print(point)
        visited.add(point)
        for i in graph[point]:
            DFS(i,visited,graph)

def findH(point,visisted,graph):
    count = 0
    if point not in graph:
        return
    if point not in visisted:
        print(point)
        visited.add(point)
        while "H" not in graph[point]:
            findH(0,visisted,graph)
            count += 1
        # for i in graph[point]:
        #     findH(i,visited,graph)
        print(count)


visited = set()
graph = {}
add_point("Y")
add_point("C")
add_point("M")
add_point("F")
add_point("A")
add_point("D")
add_point("H")
# add_road("A","'B'")
add_road("Y","C")
add_road("C","M")
add_road("Y","M")
add_road("M","H")
add_road("F","A")
add_road("A","D")
add_road("D","H")
# add_road_paced("A","B",1)
print(graph)
# DFS("A", visited, graph)
print(graph["H"])
# findH("Y",visited,graph)