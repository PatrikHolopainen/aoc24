import numpy as np

with open('test_input.txt') as f:
    lines = [list(x.strip()) for x in f.readlines()]

n_col = len(lines[0])
n_nodes = len(lines) * n_col

grid = {}

A = np.zeros((n_nodes,n_nodes))

for x,row in enumerate(lines):
    for y,cell in enumerate(row):
        grid[(x,y)] = int(cell)

for x,row in enumerate(lines):
    for y,cell in enumerate(row):
        for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (a,b) in grid and grid[(a,b)] == int(cell)+1:
                A[x*n_col+y][a*n_col+b] = 1

A_9 = np.linalg.matrix_power(A, 9)

print(np.count_nonzero(A_9))
print(np.sum(A_9))