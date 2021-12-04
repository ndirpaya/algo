def add_node(node):
    if node in graph:
        print(node, "is already in graph")
    else:
        graph[node] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edge_weighted(v1,v2,cost):
    if v1 not in graph:
        print(v1,"not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(node):
    if node not in graph:
        print(node,"is not in graph")
    else:
        graph.pop(node)
        for i in graph:
            list1 = graph[i]
            if node in list1:
                list1.remove(node)

def delete_node_weighted(node):
    if node not in graph:
        print(node, "is not in graph")
    else:
        graph.pop(node)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if node == j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


def DFS(node,visited,graph):
    if node not in graph:
        print("node not in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

# add_edge("A","B")
# add_edge("A","C")
# add_edge("A","D")
# add_edge("B","E")
# add_edge("B","D")
# add_edge("C","D")
# add_edge("D","E")
# add_edge("A", "B")
# add_edge("A", "C")
add_edge_weighted("A","B", 10)
print(graph)
DFS("B",visited,graph)