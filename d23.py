from itertools import combinations

nodes = set()
edges = []

with open('input.txt') as f:
    for l in f.readlines():
        u,v = l.strip().split('-')
        nodes.add(u)
        nodes.add(v)
        edges.append((u,v))



visited_edges = []

triangles = []

"""
# a

for k,e in enumerate(edges):
    print(k/len(edges))
    u,v = e

    for i,e1 in enumerate(visited_edges):
        u1,v1 = e1
        left_match = False
        if u1 == u:
            q1 = v1
            left_match = True
        elif v1 == u:
            q1 = u1
            left_match = True
        if left_match:
            # print("Left side connected,",u1,v1,u,v)

            for j,e2 in enumerate(visited_edges):
                u2,v2 = e2
                right_match = False
                if u2 == v:
                    q2 = v2
                    right_match = True
                elif v2 == v:
                    q2 = u2
                    right_match = True
                if right_match:
                    # print("Right side connected,",u2,v2,u,v)
                    if q1 == q2:
                        # print("It's a triangle")
                        if any([n[0] == 't' for n in [u,v,u1,v1,u2,v2]]):
                            # rint("It's a triangle with a t")
                            triangles.append((u,v,u1,v1,u2,v2))


    visited_edges.append(e)
print(len(triangles))

"""
# b

nodes = set()
for e in edges:
    nodes.add(e[0])
    nodes.add(e[1])

nodes = list(nodes)

print(len(nodes))

k = 1

womp = []

for n in nodes:
    neighbours = []
    
    for e in edges:
        u,v = e
        if u == n:
            neighbours.append(v)
        elif v == n:
            neighbours.append(u)
    neighbours = list(set(neighbours))
    neighbour_sets = list(combinations(neighbours,len(neighbours)-k))
    for ns in neighbour_sets:
        neighbour_edges = 0
        deg = len(ns)
        for e in edges:
            u,v = e
            if u in ns and v in ns:
                neighbour_edges += 1
        lcc = 2*neighbour_edges / (deg*(deg-1))
        # print(lcc,n,ns)
        if lcc == 1:
            womp.append(list(ns)+[n])
            print(ns,n)

print(','.join(sorted(womp[0])))
