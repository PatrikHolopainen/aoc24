
# Load test_input.txt grid of words
with open('input.txt') as f:
    grid = [l.strip() for l in f.readlines()]

#   0 1 2 
# 0 X X X
# 1 X X A 
# line[1][2] == A

def viable_directions(grid,row,col):
    width, height = len(grid[0]),len(grid)
    # Takes
    tl,t,tr,r,br,b,bl,l, = False,False,False,False,False,False,False,False

    directions = []

    if row - 3 >= 0:
        t = True
        directions.append('t')
    if row + 3 < height:
        b = True
        directions.append('b')
    if col - 3 >= 0:
        l = True
        directions.append('l')
    if col + 3 < width:
        r = True
        directions.append('r')
    if t and l: directions.append('tl')
    if t and r: directions.append('tr')
    if b and l: directions.append('bl')
    if b and r: directions.append('br')
    return directions

def get_4_line(grid,row,col,direction):
    # We can assume that it's a legit direction
    g = grid
    if direction == 'tl':
        return g[row][col],g[row-1][col-1],g[row-2][col-2],g[row-3][col-3]
    elif direction == 't':
        return g[row][col],g[row-1][col],g[row-2][col],g[row-3][col]
    elif direction == 'tr':
        return g[row][col],g[row-1][col+1],g[row-2][col+2],g[row-3][col+3]
    elif direction == 'r':
        return g[row][col],g[row][col+1],g[row][col+2],g[row][col+3]
    elif direction == 'br':
        return g[row][col],g[row+1][col+1],g[row+2][col+2],g[row+3][col+3]
    elif direction == 'b':
        return g[row][col],g[row+1][col],g[row+2][col],g[row+3][col]
    elif direction == 'bl':
        return g[row][col],g[row+1][col-1],g[row+2][col-2],g[row+3][col-3]
    elif direction == 'l':
        return g[row][col],g[row][col-1],g[row][col-2],g[row][col-3]



total = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'X':
            directions = viable_directions(grid,row,col)
            for d in directions:
                if ''.join(get_4_line(grid,row,col,d)) == 'XMAS':
                    total +=1

print(total)

# b

b_total = 0

def check_if_mas(grid,row,col):
    values = grid[row-1][col-1],grid[row-1][col+1],grid[row+1][col-1],grid[row+1][col+1]
    return ''.join(values) in ['MMSS','MSMS','SSMM','SMSM']

for row in range(1,len(grid)-1):
    for col in range(1,len(grid[row])-1):
        if grid[row][col] == 'A' and check_if_mas(grid,row,col): b_total +=1

print(b_total)
