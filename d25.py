
data = []

with open('input.txt') as f:
    q = []
    for i,l in enumerate(f.readlines()):
        l = l.strip()
        if l == '':
            data.append(q)
            q = []
        else:
            q.append(l)
    data.append(q)


locks = []
keys = []

for g in data:
    lock = False
    n_cols = len(g[0])
    heights = [-1]*n_cols
    if g[0][0] == '#':
        lock = True
    for i in range(n_cols):
        col = [row[i] for row in g]
        if not lock:
            col = list(reversed(col))
        height = col.index('.')
        heights[i] = height -1 
        
    if lock:
        locks.append(heights)
    else:
        keys.append(heights)

print("locks",len(locks))
print("keys",len(keys))


matches = 0

for l in locks:
    for k in keys:
        if all([l[i]+k[i] <6 for i in range(len(l))]):
            matches += 1

print(matches)