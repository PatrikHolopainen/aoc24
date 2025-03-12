import re
import time

robots= []

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        robots.append([int(x) for x in re.findall(r'-?\d+',l)])

width = 101
height = 103

a,b,c,d = 0,0,0,0


for px,py,vx,vy in robots:
    rx = (px + 100*vx)%width
    ry = (py + 100*vy)%height
    if rx < (width-1)//2 and ry < (height-1)//2: a += 1
    if rx > (width-1)//2 and ry < (height-1)//2: b += 1
    if rx < (width-1)//2 and ry > (height-1)//2: c += 1
    if rx > (width-1)//2 and ry > (height-1)//2: d += 1

print(a,b,c,d,a*b*c*d)

# b

robot_locs = [(px,py) for px,py,_,_ in robots]
robot_speeds = [(vx,vy) for _,_,vx,vy in robots]

def cprint(width,height,robot_locs):
    for y in range(height):
        for x in range(width):
            if (x,y) in robot_locs:
                print("#",end='')
            else:
                print(" ",end='')
        print()
    print()

def iterate(robot_locs,robot_speeds,width,height):
    new_locs = []
    for (px,py),(vx,vy) in zip(robot_locs,robot_speeds):
        new_locs.append(((px+vx)%width,(py+vy)%height))
    return new_locs

print(robot_locs)

start_locs = [(px,py) for px,py,_,_ in robots]

print("Starting")

# Jäätii 4150

for i in range(0):
    robot_locs = iterate(robot_locs,robot_speeds,width,height)

for i in range(10403):
    if i > 0 and all([x == z for x,z in zip(start_locs,robot_locs)]):
        print("Found cycle length: ",i)
        break

    robot_locs = iterate(robot_locs,robot_speeds,width,height)
    if i%103 == 30:
        print('\n'*10)
        cprint(width,height,robot_locs)
        print(i)
        time.sleep(0.25)
    



# 4047 HORIZONTAL
# 4107 VERTICAL
# 4150 HORIZONTAL
# 4208 VERTICAL

# 