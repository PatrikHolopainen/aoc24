import re

patterns = []

with open('input.txt') as f:
	for row in f.readlines():
		if row.strip():
			if ',' in row:
				towels = row.split(',')
				towels = [s.strip() for s in towels]
			else:
				patterns.append(row.strip())

m = '(' + ('|').join(towels) + ')*'

count = 0

for p in patterns:
	x = re.fullmatch(m,p)
	if x:
		# print(p)
		count +=1

# a 
print(count)


# b 
# print("\nB")

D = {}

def inner(target):
	if target == '':
		return 1
	if target in D:
		return D[target]
	c = 0
	for t in towels:
		if target.startswith(t):
			c += inner(target[len(t):])
			
	D[target] = c
	return c

total = 0

for p in patterns:
	z = inner(p)
	total += z
	# print(z)
# print(D)
print(total)