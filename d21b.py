from itertools import permutations

def get_permutations(s):
    perms = permutations(s)
    return [''.join(p) for p in perms]


with open('input.txt') as f:
    codes = [code.strip() for code in f.readlines()]

num_grid = {
    (0,0): '7', (0,1): '8', (0,2): '9',
    (1,0): '4', (1,1): '5', (1,2): '6',
    (2,0): '1', (2,1): '2', (2,2): '3',
    (3,0): '#', (3,1): '0', (3,2): 'A',
}

dir_grid = {
    (0,0): '#', (0,1): '^', (0,2): 'A',
    (1,0): '<', (1,1): 'v', (1,2): '>',
}



def short_paths(grid):
    shortest_paths = {}
    for item1 in grid.items():
        for item2 in grid.items():
            if not '#' in [item1[1], item2[1]]:
                path = ''
                curr_x,curr_y = item1[0]
                target_x,target_y = item2[0]
                
                x_diff = target_x - curr_x
                y_diff = target_y - curr_y

                if x_diff > 0:
                    path += 'v' * x_diff
                elif x_diff < 0:
                    path += '^' * abs(x_diff)
                if y_diff > 0:
                    path += '>' * y_diff
                elif y_diff < 0:
                    path += '<' * abs(y_diff)
                
                possible_paths = get_permutations(path)
                valid_paths = []
                for p in possible_paths:
                    x,y = item1[0]
                    k = 0
                    path_values = []
                    while k < len(p):
                        step = p[k]
                        if step == 'v':
                            x += 1
                        elif step == '^':
                            x -= 1
                        elif step == '>':
                            y += 1
                        elif step == '<':
                            y -= 1
                        path_values.append(grid[(x,y)])
                        k += 1
                    if '#' not in path_values and p not in valid_paths:
                        valid_paths.append(p)
                shortest_paths[(item1[1],item2[1])] = valid_paths
    return shortest_paths
            
# print(short_paths(num_grid))
n_paths = short_paths(num_grid)

d_paths = short_paths(dir_grid)

"""
for it in d_paths.items():
    print(it)
"""

D = {}

def inner(ins,depth): # ins = 'v<<', depth = 2
    if (ins,depth) in D:
        return D[(ins,depth)]
    if depth == 1:
        return len(ins)
    else:
        z = 'A'
        total = 0
        print(ins,depth)
        for i in ins:
            total += min([inner(p+'A',depth-1) for p in d_paths[(z,i)]])
            z = i
        D[(ins,depth)] = total
        return total

result = 0


for code in codes[:]:
    numpos = 'A'
    l = 0
    for c in code[:]:
        possible_paths = n_paths[(numpos,c)]
        shortest = float('inf')
        print(possible_paths)
        for p in possible_paths:
            q = inner(p+'A',26)
            # print(q)
            if q < shortest:
                shortest = q
                path = p
        l += shortest
        numpos = c
    print(code)
    print(l)
    result += int(code[:-1])*l
print(result)