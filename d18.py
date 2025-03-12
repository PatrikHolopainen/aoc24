import re
import numpy as np
import heapq

btes = []

with open('input.txt') as f:
    # Get both integers from each line using re
    for l in f.readlines():
        a,b = [int(i) for i in re.findall(r'\d+', l)]
        btes.append((b,a)) # Switch a,b to use row first indexing


n = 0
width = height = 71

grid= {}

for x in range(height):
    for y in range(width):
        grid[(x,y)] = '.'


for x,y in btes[:n]:
    grid[(x,y)] = '#'

A = np.full((height*width,height*width),float('inf'))

"""
# Print grid
for x in range(height):
    for y in range(height):
        print(grid[(x,y)],end='')
    print()
"""


for pair in grid.items():
    coord,value = pair
    x,y = coord
    if grid[coord] == '.':
        for neighbour in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if neighbour in grid and grid[neighbour] == '.':
                A[width*x+y,width*neighbour[0]+neighbour[1]] = 1



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

# dist,prev = dijkstra(A,0,width*height-1)

# a solution
# print(dist[width*height-1])

# print(np.array(dist).reshape(width,width))


# b 

g2 = {}
for x in range(height):
    for y in range(width):
        g2[(x,y)] = '.'

A2 = np.full((height*width,height*width),float('inf'))

for pair in grid.items():
    coord,value = pair
    x,y = coord
    if grid[coord] == '.':
        for neighbour in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if neighbour in grid and grid[neighbour] == '.':
                A2[width*x+y,width*neighbour[0]+neighbour[1]] = 1


def place_block(adj,grid,x,y):
    grid[(x,y)] = '#'
    for neighbour in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if neighbour in grid:
            adj[width*x+y,width*neighbour[0]+neighbour[1]] = float('inf')
            adj[width*neighbour[0]+neighbour[1],width*x+y] = float('inf')
    return adj,grid

dist,prev = dijkstra(A2,0,width*height-1)

def prev_to_path(prev):
    p = prev[width*height-1]
    s_path = []

    while p:
        s_path.append(p)
        p = prev[p]

    
    s_path = [0] + [m for m in list(reversed(s_path))] + [width*height-1]
    return [(z//width,z%width) for z in s_path]

t = 0
path_exists = True

current_path = prev_to_path(prev)

print(current_path)

while path_exists:
    print(t)
    x,y = btes[t]
    # Asetetaa byte
    A2,grid = place_block(A2,g2,x,y)

    # Jos byte osu meiän polulle -> uus dijkstra
    if (x,y) in current_path:
        dist,prev = dijkstra(A2,0,width*height-1)
        if dist[width*height-1] == float('inf'):
            print("No path found")
            path_exists = False

        current_path = prev_to_path(prev)
    
    # Jos dijkstra antaa tuloksen, mennää vaa taas eteepäi
    t +=1

print(t)