with open('input.txt') as f:
    a = f.readline().strip()

l = []

class Slot:
    # Set an ID value for each slot
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return f"Slot({self.id})"

id_counter = 0

for i,k in enumerate(a):
    if i%2 == 0:
        for _ in range(int(k)):
            l.append(Slot(id_counter))
        id_counter += 1
    else:
        for _ in range(int(k)):
            l.append(None)


i = 0
while i < len(l):
    print(i)
    if l[i] is None:
        while l[-1] is None:
            l.pop()
        if i < len(l): l[i] = l.pop()
    i += 1

print(sum([i*x.id for i,x in enumerate(l)]))