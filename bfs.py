from collections import deque
graph = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':['F'], 'E':['F'], 'F':[]}
def bfs_shortest_path(graph, start, end):
    queue=deque([(start,[start])])
    visited = [] 
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        if current not in visited:
            
    
result = bfs_shortest_path(graph, 'A', 'F')
print(result)