with open('input.txt') as f:
    stones = [int(x) for x in f.readline().strip().split()]

D = {}

def new_stones(stones):
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
        elif len(str(s)) %2==0:
            st = str(s)
            left = int(st[:len(st)//2])
            right = int(st[len(st)//2:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(s*2024)
    return new_stones

"""

for i in range(25):
    stones = new_stones(stones)
    
print(len(stones))
"""
# b

D = {}

def val_k(s,k):
    if (s,k) in D:
        return D[(s,k)]
    elif k == 1:
        D[(s,k)] = 1
        return 1
    else:
        if s == 0:
            D[(s,k)] = val_k(1,k-1)
            return D[(s,k)]
        elif len(str(s)) %2==0:
            st = str(s)
            left = int(st[:len(st)//2])
            right = int(st[len(st)//2:])
            D[(s,k)] = val_k(left,k-1) + val_k(right,k-1)
            return D[(s,k)]
        else:
            D[(s,k)] = val_k(s*2024,k-1)
            return D[(s,k)]

total = 0
for s in stones:
    total += val_k(s,76)

# print(D)

print(total)
