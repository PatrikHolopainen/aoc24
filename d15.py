

grid_data = []
route_data = ''

with open('input.txt') as f:
    br = False
    s = ''
    for l in f.readlines():
        row = l.strip()
        if len(row) == 0:
            br = True
        elif br:
            route_data += row
        else:
            grid_data.append(row)

g = {}

cx,cy = 0,0

for x,row in enumerate(grid_data):
    for y,c in enumerate(row):
        if c == '@':
            cx,cy = x,y
        g[(x,y)] = c

print(len(route_data))

i = 0

def target(x,y,d):
    if d == '^':
        return x-1,y
    elif d == 'v':
        return x+1,y
    elif d == '<':
        return x,y-1
    elif d == '>':
        return x,y+1
    
def can_move(x,y,d):
    tx,ty = target(x,y,d)
    if g[(tx,ty)] == '.':
        return True
    elif g[(tx,ty)] == 'O':
        if can_move(tx,ty,d):
            g[(tx,ty)] = '.'
            g[target(tx,ty,d)] = 'O'
            return True
        else:
            return False
    elif g[(tx,ty)] == '#':
        return False

width = max(g.items(),key=lambda x: x[0][0])[0][0] +1
height = max(g.items(),key=lambda x: x[0][1])[0][1] +1

while i < len(route_data):
    # print(i)
    if False:
        for x in range(width):
            for y in range(height):
                print(g[(x,y)],end='')
            print()

    dir = route_data[i]
    if can_move(cx,cy,dir):
        g[(cx,cy)] = '.'
        cx,cy = target(cx,cy,dir)
        g[(cx,cy)] = '@'
    i += 1
    
total = 0

for z in g.items():
    if z[1] == 'O':
        total += z[0][0]*100 + z[0][1]

print(total)

# b

# Generating new grid

new_grid_data = []

for row in grid_data:
    new_row = []
    for x in row:
        if x == '#':
            new_row.append('#')
            new_row.append('#')
        elif x == '.':
            new_row.append('.')
            new_row.append('.')
        elif x == '@':
            new_row.append('@')
            new_row.append('.')
        elif x == 'O':
            new_row.append('[')
            new_row.append(']')

    new_grid_data.append(new_row)

g2 ={}

for x,row in enumerate(new_grid_data):
    for y,c in enumerate(row):
        if c == '@':
            cx,cy = x,y
        g2[(x,y)] = c

print(g2)

i = 0


def box_target(x,y1,y2,d):
    if d == '^':
        return x-1,y1,y2
    elif d == 'v':
        return x+1,y1,y2
    elif d == '<':
        return x,y1-1,y2-1
    elif d == '>':
        return x,y1+1,y2+1

def move_lookup(x,y1,y2,d):
    if d == '<':
        if g2[(x,y1-1)] == '.':
            return True
        elif g2[(x,y1-1)] == '[':
                return True
        elif g2[(x,y1-1)] == ']':
                return True
        
        return False
    elif d == '>':
        if g2[(x,y2+1)] == '.':
            return True
        elif g2[(x,y2+1)] == '[':
            if move_lookup(x,y2+1,y2+2,d):
                return True
        elif g2[(x,y2+1)] == ']':
            if move_lookup(x,y1-1,y2-1,d):
                return True
        return False
    elif d == '^':
        if g2[(x-1,y1)] == '.' and g2[(x-1,y2)] == '.':
            return True
        elif g2[(x-1,y1)] == '[':
            if move_lookup(x-1,y1,y2,d):
                return True
        
        can_move_left = False
        can_move_right = False
        
        if g2[(x-1,y1)] == ']':
            if move_lookup(x-1,y1-1,y1,d):
                can_move_left = True
        if g2[(x-1,y2)] == '[':
            if move_lookup(x-1,y2,y2+1,d):
                can_move_right = True
        if g2[(x-1,y1)] == '.':
            can_move_left = True
        if g2[(x-1,y2)] == '.':
            can_move_right = True
        
        if can_move_left and can_move_right:
            return True
        return False
    elif d == 'v':
        
        if g2[(x+1,y1)] == '.' and g2[(x+1,y2)] == '.':
            print("Seeing empty down")
            return True
        elif g2[(x+1,y1)] == '[':
            print("seeing box start down")
            if move_lookup(x+1,y1,y2,d):
                return True
        
        can_move_left = False
        can_move_right = False
        
        if g2[(x+1,y1)] == ']':
            if move_lookup(x+1,y1-1,y1,d):
                can_move_left = True
        if g2[(x+1,y1)] == '.':
            can_move_left = True
        if g2[(x+1,y2)] == '.':
            can_move_right = True
        if g2[(x+1,y2)] == '[':
            print("This is what I should see",x,y1,y2,d)
            if move_lookup(x+1,y2,y2+1,d):
                print("Did we succeed?",x,y1,y2,d)
                can_move_right = True
        
        
        if can_move_left and can_move_right:
            return True
        return False
    return False
   
def can_move_box(x,y1,y2,d):
    # print("Trying to move the box",x,y1,y2,"towards",d)
    if d == '<':
        if g2[(x,y1-1)] == '.':
            # print("Left was empty")
            g2[(x,y1-1)] = '['
            g2[(x,y1)] = ']'
            g2[(x,y+1)] = '.'
            # print("Moved box",)
            return True
        elif g2[(x,y1-1)] == '[':
            # print("Left is blocked by box start")
            if can_move_box(x,y1-1,y2-1,d):
                g2[(x,y1-1)] = ']'
                g2[(x,y1)] = '['
                g2[(x,y1+1)] = '.'
                return True
        elif g2[(x,y1-1)] == ']':
            # print("Left is blocked by box end")
            if can_move_box(x,y1-1,y2-1,d):
                g2[(x,y1-1)] = '['
                g2[(x,y1)] = ']'
                g2[(x,y1+1)] = '.'
                return True
        
        return False
    elif d == '>':
        if g2[(x,y2+1)] == '.':
            
            g2[(x,y2)] = '['
            g2[(x,y2+1)] = ']'
            g2[(x,y1)] = '.'
            # print("Moved box",)
            return True
        elif g2[(x,y2+1)] == '[':
            
            if can_move_box(x,y2+1,y2+2,d):
                g2[(x,y2)] = '['
                g2[(x,y2+1)] = ']'
                g2[(x,y1)] = '.'
                return True
        elif g2[(x,y2+1)] == ']':
            if can_move_box(x,y1-1,y2-1,d):
                g2[(x,y2)] = '['
                g2[(x,y2+1)] = ']'
                g2[(x,y1)] = '.'
                return True
        
        return False
    elif d == 'v':
        if g2[(x+1,y1)] == '.' and g2[(x+1,y2)] == '.':
            g2[(x+1,y1)] = '['
            g2[(x+1,y2)] = ']'
            g2[(x,y1)] = '.'
            g2[(x,y2)] = '.'
            return True
        elif g2[(x+1,y1)] == '[':
            if can_move_box(x+1,y1,y2,d):
                g2[(x+1,y1)] = '['
                g2[(x+1,y2)] = ']'
                g2[(x,y1)] = '.'
                g2[(x,y2)] = '.'
                return True

        can_move_left = False
        can_move_right = False
        
        if g2[(x+1,y1)] == ']':
            if can_move_box(x+1,y1-1,y1,d):
                can_move_left = True
        if g2[(x+1,y2)] == '[':
            if can_move_box(x+1,y2,y2+1,d):
                can_move_right = True
        
        if g2[(x+1,y1)] == '.':
            can_move_left = True
        if g2[(x+1,y2)] == '.':
            can_move_right = True

        if can_move_left and can_move_right:
            g2[(x+1,y1)] = '['
            g2[(x+1,y2)] = ']'
            g2[(x,y1)] = '.'
            g2[(x,y2)] = '.'
            return True
        return False

    elif d == '^':
        if g2[(x-1,y1)] == '.' and g2[(x-1,y2)] == '.':
            g2[(x-1,y1)] = '['
            g2[(x-1,y2)] = ']'
            g2[(x,y1)] = '.'
            g2[(x,y2)] = '.'
            return True
        elif g2[(x-1,y1)] == '[':
            if can_move_box(x-1,y1,y2,d):
                g2[(x-1,y1)] = '['
                g2[(x-1,y2)] = ']'
                g2[(x,y1)] = '.'
                g2[(x,y2)] = '.'
                return True
        
        can_move_left = False
        can_move_right = False
        
        if g2[(x-1,y1)] == ']':
            if can_move_box(x-1,y1-1,y1,d):
                can_move_left = True
        if g2[(x-1,y2)] == '[':
            if can_move_box(x-1,y2,y2+1,d):
                can_move_right = True
        if g2[(x-1,y1)] == '.':
            can_move_left = True
        if g2[(x-1,y2)] == '.':
            can_move_right = True
        
        if can_move_left and can_move_right:
            g2[(x-1,y1)] = '['
            g2[(x-1,y2)] = ']'
            g2[(x,y1)] = '.'
            g2[(x,y2)] = '.'
            return True
        return False
    return False
        



width = max(g2.items(),key=lambda x: x[0][0])[0][0] +1
height = max(g2.items(),key=lambda x: x[0][1])[0][1] +1

i = 0

while i < len(route_data):
    dir = route_data[i]
    if False:
        for x in range(width):
            for y in range(height):
                c = g2[(x,y)]
                if c == '.': c=' '
                if c == '@': c=dir
                print(c,end='')
            print()
        input(f"looking good {i}")
        print("Direction:",dir)
        

    tx,ty = target(cx,cy,dir)
    moves = False
    if g2[(tx,ty)] == '.':
        g2[(cx,cy)] = '.'
        cx,cy = tx,ty
        g2[(cx,cy)] = '@'
    elif g2[(tx,ty)] == '[':
        print("lookup for box start",move_lookup(tx,ty,ty+1,dir))
        if move_lookup(tx,ty,ty+1,dir) and can_move_box(tx,ty,ty+1,dir):
            g2[(cx,cy)] = '.'
            cx,cy = tx,ty
            g2[(cx,cy)] = '@'
            
    elif g2[(tx,ty)] == ']':
        if move_lookup(tx,ty-1,ty,dir) and can_move_box(tx,ty-1,ty,dir):
            g2[(cx,cy)] = '.'
            cx,cy = tx,ty
            g2[(cx,cy)] = '@'
    i += 1

for x in range(width):
    for y in range(height):
        print(g2[(x,y)],end='')
    print()

locs = []

for z in g2.items():
    if z[1] == '[':
        x,y = z[0]
        locs.append([(x,y),(x,y+1)])
q = 0

for a,b in locs:
    horizontal = a[1]
    vertical = a[0]
    # print(a,b,horizontal,vertical,horizontal+vertical*100)
    q+= horizontal + vertical*100
print(q)