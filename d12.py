
grid = {}



with open('input.txt') as f:
    for x,row in enumerate(f.readlines()):
        for y,cell in enumerate(row.strip()):
            grid[(x,y)] = cell

width,height = x+1,y+1

searched_cells = []

# ALOTETAAN B KOHTAAA!!!

def search_area(grid,x,y):
    area_code = grid[(x,y)]
    area = [(x,y)]
    i = 0
    # Direction, coordinates
    fence = 0
    fences = []

    # 0 ylös, 1 alas, 2 vasen, 3 oikea
    while i < len(area):
        x,y = area[i]
        for direction,neighbour in enumerate([(x-1,y),(x+1,y),(x,y-1),(x,y+1)]):
            if neighbour not in area:
                if neighbour in grid and grid[neighbour] == area_code:
                    area.append(neighbour)
                else:
                    fences.append((x,y,direction))
                    fence += 1
        i+=1
    
    # Ylöspäi fences
    up_fences = [f for f in fences if f[2]==0]
    down_fences = [f for f in fences if f[2]==1]
    left_fences = [f for f in fences if f[2]==2]
    right_fences = [f for f in fences if f[2]==3]

    sides = 0
    if len(up_fences) > 0:
        up_fences.sort(key=lambda z: z[1])
        up_fences.sort(key=lambda z: z[0])
        edges  = 1
        currx,curry = up_fences[0][0],up_fences[0][1]
        for nextx,nexty,_ in up_fences[1:]:
            if nextx != currx:
                edges += 1
            elif nexty != curry+1:
                edges += 1
            currx,curry = nextx,nexty
        # print("Up fences",up_fences,"Edges",edges)
        sides += edges
    if len(down_fences) > 0:
        down_fences.sort(key=lambda z: z[1])
        down_fences.sort(key=lambda z: z[0])
        edges  = 1
        currx,curry = down_fences[0][0],down_fences[0][1]
        for nextx,nexty,_ in down_fences[1:]:
            if nextx != currx:
                edges += 1
            elif nexty != curry+1:
                edges += 1
            currx,curry = nextx,nexty
        # print("Down fences",down_fences,"Edges",edges)
        sides += edges
    if len(left_fences) > 0:
        left_fences.sort(key=lambda z: z[0])
        left_fences.sort(key=lambda z: z[1])
        edges  = 1
        currx,curry = left_fences[0][0],left_fences[0][1]
        for nextx,nexty,_ in left_fences[1:]:
            if nexty != curry:
                edges += 1
            elif nextx != currx+1:
                edges += 1
            currx,curry = nextx,nexty
       # print("Left fences",left_fences,"Edges",edges)
        sides += edges
    if len(right_fences) > 0:
        right_fences.sort(key=lambda z: z[0])
        right_fences.sort(key=lambda z: z[1])
        edges  = 1
        currx,curry = right_fences[0][0],right_fences[0][1]
        for nextx,nexty,_ in right_fences[1:]:
            if nexty != curry:
                edges += 1
            elif nextx != currx+1:
                edges += 1
            currx,curry = nextx,nexty
        # print("Right fences",right_fences,"Edges",edges)
        sides += edges
    
    
    

    cost = len(area) * sides

    # print("Cost",cost,"Area",area,"Sides",sides)

    # Olisko nyt et käydää vasemmalt oikeelle ja lasketaa yhtenäiset sticks?
    # cost = fence * len(area)
    return area,cost

row,col = 0,0
total_cost = 0
while row < height:
    col = 0
    while col < width:
        if (row,col) not in searched_cells:
            area,cost = search_area(grid,row,col)
            total_cost += cost
            for coord in area: searched_cells.append(coord)
        col +=1
    row +=1

print(total_cost)