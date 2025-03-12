import time

g = {}


with open('input.txt') as f:
    lines = f.readlines()
    for x,line in enumerate(lines):
         line = line.strip()
         for y,c in enumerate(line):
            g[(x,y)] = c
            if c == 'S':
                s = (x,y)
            elif c == 'E':
                e = (x,y)


path = [s]

curr = s

while curr != e:
    # print(path)
    x,y = curr
    if  (x+1,y) not in path and g[(x+1,y)] in ['.','E']:
        curr = (x+1,y)
        path.append(curr)
    elif (x-1,y) not in path and g[(x-1,y)] in ['.','E']:
        curr = (x-1,y)
        path.append(curr)
    elif (x,y+1) not in path and g[(x,y+1)] in ['.','E']:
        curr = (x,y+1)
        path.append(curr)
    elif (x,y-1) not in path and g[(x,y-1)] in ['.','E']:
        curr = (x,y-1)
        path.append(curr)

# print(path)

picoseconds = len(path)

print(picoseconds)

distances = list(reversed(range(picoseconds)))

threshold = 100

count = 0

for k in range(picoseconds):
    x,y = path[k]
    for cheat in [[(x-1,y),(x-2,y)],[(x+1,y),(x+2,y)],[(x,y-1),(x,y-2)],[(x,y+1),(x,y+2)]]:
        if cheat[0] in g and cheat[1] in g and g[cheat[0]] == '#' and cheat[1] in path:
            idx = path.index(cheat[1])
            improvement = distances[k] - (distances[idx] + 2)
            if improvement >= threshold:
                count +=1


print(count)


# b

count = 0

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for k in range(picoseconds):
    print(k/picoseconds)
    x,y = path[k]
    remaining_path = path[k:]
    targets = []
    for zx in range(-20,21):
        for zy in range(-20,21):
            xt = x + zx
            yt = y + zy
            if (xt,yt) in remaining_path:
                d = dist((x,y),(xt,yt))
                if d <= 20:
                    targets.append((xt,yt))
    for t in targets:
        idx = path.index(t)
        improvement = distances[k] - (distances[idx] + dist((x,y),t))
        if improvement >= threshold:
            # print(k,x,y,t)
            count +=1
print(count)