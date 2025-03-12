
nodes = {}

gates = []

with open('input.txt') as f:
    for l in f.readlines():
        l = l.strip()
        if ':' in l:
            key = l.split(':')[0]
            value = int(l.split(':')[1].strip())
            nodes[key] = value
        elif '->' in l:
            words = l.split(' ')
            gates.append([words[0].strip(),words[1].strip(),words[2].strip(),words[4].strip()])



remaining_gates = gates[:]
nodes_b = nodes.copy()

while remaining_gates:
    for g in remaining_gates:
        if g[0] in nodes and g[2] in nodes:
            if g[1] == 'AND':
                nodes[g[3]] = nodes[g[0]] & nodes[g[2]]
            elif g[1] == 'OR':
                nodes[g[3]] = nodes[g[0]] | nodes[g[2]]
            elif g[1] == 'XOR':
                nodes[g[3]] = nodes[g[0]] ^ nodes[g[2]]
            remaining_gates.remove(g)


b = ''

zs = []

for it in sorted([q for q in nodes.items() if q[0][0]=='z'],key=lambda x: -int(x[0][1:])):
    b += str(it[1])



bx = ''
by = ''
for it in nodes_b.items():
    if it[0][0] == 'x':
        bx += str(it[1])
    if it[0][0] == 'y':
        by += str(it[1])


bx = ''.join(list(reversed(bx)))
by = ''.join(list(reversed(by)))

print("bx",bx)
print("by",by)

x = int(bx,2)
y = int(by,2)
print(b)
print(str(bin(x+y))[2:])

print("\n\n")


def check_structure(k):
    x = 'x' + str(k).zfill(2)
    y = 'y' + str(k).zfill(2)
    z = 'z' + str(k).zfill(2)

    # Check that all relevant gates exist
    a1 = [g for g in gates if ((g[0] == x and g[2] == y) or (g[0] == y and g[2] == x)) and g[1] == 'AND']
    assert len(a1) > 0, "No AND1 gate found in for x{} and y{}".format(k,k)
    a1 = a1[0]
    x1 = [g for g in gates if ((g[0] == x and g[2] == y) or (g[0] == y and g[2] == x)) and g[1] == 'XOR']
    assert len(x1) > 0, "No XOR1 gate found in for x{} and y{}".format(k,k)
    x1 = x1[0]

    print(a1,x1)
    x2 = [g for g in gates if g[3] == z and (g[0] == x1[3] or g[2] == x1[3]) and g[1] == 'XOR']
    assert len(x2) > 0, "No XOR2 gate found in for x{} and y{}".format(k,k)
    x2 = x2[0]


    if x2[0] == x1[3]:
        cin = x2[2]
    elif x2[2] == x1[3]:
        cin = x2[0]
    
    assert cin, "No CIN gate found for x{} and y{}".format(k,k)

    a2 = [g for g in gates if ((g[0] == x1[3] and g[2] == cin) or (g[0] == cin and g[2] == x1[3])) and g[1] == 'AND']
    assert len(a2) > 0, "No AND2 gate found in for x{} and y{}".format(k,k)
    a2 = a2[0]

    
    out = [g for g in gates if (g[0] == a1[3] and g[2] == a2[3] or g[0] == a2[3] and g[2] == a1[3]) and g[1] == 'OR']
    assert len(out) > 0, "No OUT gate found in for x{} and y{}".format(k,k)
    out = out[0]

    print("Gate structure seems good at k = ",k)
    return a1,a2,cin,out,x1,x2




l = ["btb", "mwp", "z30", "rdg", "z23", "rmj", "cmv", "z17"]


z = ','.join(sorted(l))
print(z)