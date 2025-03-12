
# Read input.txt that has just two columns of numbers

# 1 2
# 3 4


# Read the file
a,b = [],[]
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        n,m = [int(x) for x in line.split()]
        a.append(n), b.append(m)

a,b = sorted(a),sorted(b)
diffs = 0
for i in range(len(a)):
    diffs += abs(a[i]-b[i])

print(diffs)


# b
similarity = 0

for x in a:
    similarity += b.count(x) * x

print(similarity)