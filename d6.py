import re

with open('input.txt') as f:
    grid = []
    for row in f.readlines():
        grid.append([x for x in row.strip()])

def is_next_step_out(grid,row,col,direction):
    if direction == 'n':
        return row - 1 < 0
    elif direction == 'e':
        return col + 1 >= len(grid[0])
    elif direction == 's':
        return row + 1 >= len(grid)
    elif direction == 'w':
        return col - 1 < 0

def is_next_step_wall(grid,row,col,direction):
    if direction == 'n':
        return grid[row-1][col] == '#'
    elif direction == 'e':
        return grid[row][col+1] == '#'
    elif direction == 's':
        return grid[row+1][col] == '#'
    elif direction == 'w':
        return grid[row][col-1] == '#'

def turn_right(direction):
    if direction == 'n':
        return 'e'
    elif direction == 'e':
        return 's'
    elif direction == 's':
        return 'w'
    elif direction == 'w':
        return 'n'

def is_next_step_visited(grid,row,col,direction):
    if direction == 'n':
        return grid[row-1][col] == 'n'
    elif direction == 'e':
        return grid[row][col+1] == 'e'
    elif direction == 's':
        return grid[row+1][col] == 's'
    elif direction == 'w':
        return grid[row][col-1] == 'w'


starting_row,starting_col = 0,0

for row,_ in enumerate(grid):
    for col,_ in enumerate(grid[row]):
        if grid[row][col] == '^':
            starting_row,starting_col = row,col
            break

# B, make an iteration of adding one more obstacle.

starting_grid = [[y for y in x] for x in grid]


def reset_grid(starting_grid,starting_row,starting_col):
    return [[y for y in x] for x in starting_grid],starting_row,starting_col


total = 0

def cprint(grid):
    for row in grid:
        print("".join(row))

total_iterations = len(grid)*len(grid[0])

max_steps = 100_000


for row in range(len(grid)):
    for col in range(len(grid[0])):
        print("Iteration",row*len(grid[0])+col,"/",total_iterations,row,col)
        grid,curr_row,curr_col = reset_grid(starting_grid,starting_row,starting_col)
        steps = 0
        if grid[row][col] == '.':
            grid[row][col] = '#'
            out_of_bounds = False
            loop = False
            direction = 'n'

            # print("Starting routing...\n")

            while not out_of_bounds and not loop and steps < max_steps:
                if is_next_step_out(grid,curr_row,curr_col,direction):
                    # print("Next step is out of bounds")
                    # cprint(grid)
                    out_of_bounds = True
                    grid[curr_row][curr_col] = 'n'
                else:
                    if is_next_step_wall(grid,curr_row,curr_col,direction):
                        direction = turn_right(direction)
                    else:
                        if is_next_step_visited(grid,curr_row,curr_col,direction):
                            loop = True
                        else:
                            if direction == 'n':
                                grid[curr_row][curr_col] = 'n'
                                curr_row -= 1
                            elif direction == 'e':
                                grid[curr_row][curr_col] = 'e'
                                curr_col += 1
                            elif direction == 's':
                                grid[curr_row][curr_col] = 's'
                                curr_row += 1
                            elif direction == 'w':
                                grid[curr_row][curr_col] = 'w'
                                curr_col -= 1
                steps += 1
                if steps == max_steps: loop = True
            if loop:
                total += 1



# print(len(re.findall("[nesw]",str(grid))))

print(total)