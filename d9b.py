with open('input.txt') as f:
    a = f.readline().strip()

l = []

class Slot:
    # Set an ID value for each slot
    def __init__(self, id,size):
        self.id = id
        self.size = size
    def __repr__(self):
        if self.id or self.id==0:
            return str(self.id)*self.size
        else:
            return "."*self.size
            

id_counter = 0

for i,k in enumerate(a):
    if i%2 == 0:
        l.append(Slot(id_counter,int(k)))
        id_counter += 1
    else:
        if int(k) > 0: l.append(Slot(None,int(k)))



max_bid = max([z for z in l if z.id],key=lambda x: x.id)

def combine_gaps(li):
    new_li = []
    i = 0
    counter = 0
    while i < len(li):
        if li[i].id != None:
            if counter > 0:
                new_li.append(Slot(None,counter))
                counter = 0
            new_li.append(li[i])
        elif li[i].id == None:
            counter += li[i].size
        i+=1
    return new_li

# li_test = [Slot(0,1),Slot(None,1),Slot(1,3),Slot(None,3),Slot(None,2),Slot(2,1)]
# print(combine_gaps(li_test))


bids = reversed(list(range(0,max_bid.id+1)))

for bid in bids:
    print
    curr_bid = l[[z.id for z in l].index(bid)]
    partial_l = l[:l.index(curr_bid)]
    i = 0
    swapped = False
    while i < len(partial_l) and not swapped:
        target = partial_l[i]
        if target.id == None:
            if target.size == curr_bid.size:
                partial_l[i] = curr_bid
                swapped = True
            elif target.size > curr_bid.size:
                partial_l[i] = curr_bid
                partial_l.insert(i+1,Slot(None,target.size-curr_bid.size))
                swapped = True
        
        i +=1
    if swapped:
        l = partial_l + [Slot(None,curr_bid.size)] + l[l.index(curr_bid)+1:]
    l = combine_gaps(l)
print(l)

total = 0

idx = 0
for s in l:
    for t in range(s.size):
        if s.id == None:
            total+=0
        else:
            total+=s.id*idx
        idx+=1

print(total)

"""
for i,s in enumerate(l[::-1]):
    print(l)
    
    k = len(l) - i
    if s.id != None:
        print("Finding a place for ",s)
        z = 0
        swapped = False
        while z < k and not swapped: 
            prospect = l[z]
            if prospect.id == None and prospect.size == s.size:
                print("Perfect match, swapping",s,"with",prospect,"at",z,"and",k)
                l[z] = s
                l[k] = Slot(None,s.size)
                swapped = True
            elif prospect.id == None and prospect.size > s.size:
                print("Found partial fit.")
                l[z] = s
                l.insert(z+1,Slot(None,prospect.size-s.size))
                l[k] = Slot(None,s.size)
                swapped = True
            z +=1
    

print(l)
"""