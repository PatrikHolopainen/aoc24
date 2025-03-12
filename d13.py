import re
import sympy

a = (0,0)
b = (0,0)
prize = (0,0)

data = []

with open('input.txt') as f:
    for row in f.readlines():
        x = row.strip()
        if len(x) > 0:
            if "A" in x:
                # Find with regex 1-unlimited digites that follow plus signs (two cases)
                a = tuple(map(int,re.findall(r'\d+',x)))
            elif "B" in x:
                b = tuple(map(int,re.findall(r'\d+',x)))
            else:
                prize = tuple(map(int,re.findall(r'\d+',x)))
                data.append([a,b,prize])

from sympy.abc import x, y, z

costs = 0

for a,b,prize in data:
    
    prize = (prize[0]+10000000000000,prize[1]+10000000000000)

    res = sympy.solve([x * a[0] + y * b[0] - prize[0], x * a[1] + y * b[1] - prize[1]],[x,y],dict=True) 
    p,q = res[0][x],res[0][y]
    if p.is_integer and q.is_integer:
        costs += p*3 + q*1
        # print("Costs",costs)
        
print(costs)