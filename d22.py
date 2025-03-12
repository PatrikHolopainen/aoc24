with open('input.txt') as f:
    secret_numbers = [int(l.strip()) for l in f.readlines()]

m = 16777216

def op(x):
    z = x*64
    sec = x^z
    sec = sec %m

    z = sec // 32
    sec = sec^z
    sec = sec %m

    z = sec*2048
    sec = sec^z
    sec = sec %m

    return sec

total = 0

for sn in secret_numbers:
    q = sn
    for _ in range(2000):
        q = op(q)
    total +=q

print(total)

# b

D = {}

for sn in secret_numbers[:]:
    sn_d = {}

    # sn_window = [None,None,None,sn]
    diffs = [None,None,None,None]

    val = sn
    price = val %10

    for i in range(2000):
        val = op(val)
        new_price = val %10
        diffs = [diffs[1],diffs[2],diffs[3],new_price - price]
        price = new_price
        # print(val,diffs,new_price)
        
        if all([x != None for x in diffs]) and tuple(diffs) not in sn_d:
            # if tuple(diffs) == (-2,1,-1,3):
                # print("foynd",val,price)
            sn_d[tuple(diffs)] = price
    # for it in sn_d.items():
        # print(it)
    
    for it in sn_d.items():
        if it[0] not in D:
            D[it[0]] = it[1]
        else:
            D[it[0]] += it[1]
    # print(D[(-2,1,-1,3)])
    

its = sorted(D.items(),key= lambda x: x[1])

print(its[-1])

