import numpy as np
import heapq

g = {}

s = (0,0)
e = (0,0)

with open('input.txt') as f:
    for row,l in enumerate(f.readlines()):
        for col,c in enumerate(l.strip()):
            g[(row,col)] = c
            if c == 'S':
                s = (row,col)
                g[(row,col)] = '.'
            elif c == 'E':
                e = (row,col)
                g[(row,col)] = '.'            

nodes= [s,e]


width = max(g.items(),key=lambda x: x[0][0])[0][0] +1
height = max(g.items(),key=lambda x: x[0][1])[0][1] +1


for x in range(1,width-1):
    for y in range(1,height-1):
        if g[(x,y)] == '.':
            up,down,left,right = g[(x-1,y)],g[(x+1,y)],g[(x,y-1)],g[(x,y+1)]
            if (up == '.' or down == '.') and (left == '.' or right == '.'):
                if (x,y) not in nodes:
                    nodes.append((x,y))


edges = []

A = np.full((len(nodes), len(nodes)), float('inf'))
B = np.full((len(nodes), len(nodes)), float('inf'))



for i,n1 in enumerate(nodes):
    for j,n2 in enumerate(nodes):
        if i != j:
            if n1[0] == n2[0]:
                if all([g[(n1[0],y)] == '.' for y in range(min(n1[1],n2[1]),max(n1[1],n2[1]))]):
                    distance = max(n1[1],n2[1]) - min(n1[1],n2[1])
                    if i == 0: print(n1,n2,distance)
                    A[i,j] = distance +1000
                    B[i,j] = distance +1000
            elif n1[1] == n2[1]:
                if all([g[(x,n1[1])] == '.' for x in range(min(n1[0],n2[0]),max(n1[0],n2[0]))]):
                    distance = max(n1[0],n2[0]) - min(n1[0],n2[0])
                    A[i,j] = distance + 1000
                    B[i,j] = distance + 1000
        else:
            A[i,j] = 0
            B[i,j] = 0


def dijkstra(adj_matrix, start, end,max_dist=float('inf')):
    n = adj_matrix.shape[0]
    dist = np.full(n, float('inf'))
    prev = np.full(n, None)
    dist[start] = 0
    prev[start] = None
    visited = [False] * n
    
    priority_queue = [(0, start)] 
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        
        if current_dist > max_dist:
            return np.full(n, float('inf')),prev

        if visited[current_node]:
            continue
        
        visited[current_node] = True
        
        if current_node == end:
            return dist,prev
        
        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] != float('inf'):
                new_dist = current_dist + adj_matrix[current_node][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_dist, neighbor))
    
    return dist,prev


n = A.shape[0]

dist,prev = dijkstra(A, 0, 1)

k_nodes = []

distance_to_k = {

}

shorties = []


for k in range(1,n):
    print(k/n)
    dist_x,prev_x = dijkstra(A, 0, k, dist[1])

    if dist_x[k] < dist[1]:
        dist_y,prev_y = dijkstra(A, k, 1,dist[1])
        
        combo_distance = dist_x[k] + dist_y[1]

        if dist[1] == combo_distance:
            p = prev_y[1]
            s_path = []
            while p:
                s_path.append(p)
                p = prev_y[p]
            p = prev_x[k]
            while p:
                s_path.append(p)
                p = prev_x[p]
            s_path = [0] + [m for m in list(reversed(s_path))] + [1]
            if s_path not in shorties: shorties.append(s_path)
            k_nodes.append(k)


print("KDNOES")
for k in k_nodes:
    print(nodes[k])

print("Shorties",shorties)
"""
p = prev[1]
s_path = []

while p:
    s_path.append(p)
    p = prev[p]

s_path = [0] + [m for m in list(reversed(s_path))] + [1]

s_path_dist = {n:int(dist[n]) for n in s_path}


print(s_path_dist)

shortest_path = dist[1]

print(f"Shortest path from node 0 to 1: {shortest_path}")

"""

g2 = {}

for p in shorties:
    for j in range(1,len(p)):
        i = j-1
        a,b = nodes[p[i]],nodes[p[j]]
        for row in range(min([a[0],b[0]]),max([a[0],b[0]])+1):
            for col in range(min([a[1],b[1]]),max([a[1],b[1]])+1):
                g2[(row,col)] = 'O'

print(len(g2.items()))


"""

c_node = 0
# Get all indexes from A[0] where value is larger than 0 but smaller than infinity
indexes = np.where((A[0] > 0) & (A[0] < float('inf')))[0]


MAX_DISTANCE = shortest_path
print(MAX_DISTANCE)

global short_paths
short_paths = []

def inner(node,path,d):
    if node == 1 and d == MAX_DISTANCE:
        global short_paths
        short_paths.append(path)
        return True
    elif d > MAX_DISTANCE:
        return False
    if node in s_path_dist and d > s_path_dist[node]:
        return False
    elif MAX_DISTANCE - d < 2000 and nodes[node][0] != nodes[1][0] and nodes[node][1] != nodes[1][1]:
        return False
    else:
        indexes = np.where((A[node] > 0) & (A[node] < float('inf')))[0]
        for i in indexes:
            i = int(i)
            if i not in path:
                inner(i,path[:] + [i],A[node][i]+d)
        
inner(0,[0],0)

print(short_paths)

g2 = {}

for p in short_paths:
    for j in range(1,len(p)):
        i = j-1
        a,b = nodes[p[i]],nodes[p[j]]
        for row in range(min([a[0],b[0]]),max([a[0],b[0]])+1):
            for col in range(min([a[1],b[1]]),max([a[1],b[1]])+1):
                g2[(row,col)] = 'O'

print(len(g2.items()))

"""