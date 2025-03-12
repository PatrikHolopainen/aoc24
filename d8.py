grid = {}

with open('input.txt') as f:
    l = f.readlines()
    for x,row in enumerate(l):
        for y,char in enumerate(row.strip()):
            grid[(x,y)] = char

frequencies = [f for f in list(set(grid.values())) if f != '.']

antinodes = []
for f in frequencies:
    antennas = [it for it in grid.items() if it[1] == f]
    for i,a in enumerate(antennas):
        for j,b in enumerate(antennas[i:]):
            if a != b:
                x1,y1 = a[0]
                x2,y2 = b[0]
                antinodes.append(a[0])
                antinodes.append(b[0])
                direction1 = ((x1-x2),(y1-y2))
                direction2 = ((x2-x1),(y2-y1))
                loc1 = a[0]
                while loc1 in grid:
                    antinodes.append(loc1)
                    loc1 = (loc1[0]+direction1[0],loc1[1]+direction1[1])
                loc2 = b[0]
                while loc2 in grid:
                    antinodes.append(loc2)
                    loc2 = (loc2[0]+direction2[0],loc2[1]+direction2[1])

print(len(set(antinodes)))