import re

with open('input.txt') as f:
    s = f.read().strip()

results = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)",s)

sum = 0
for r in results:
    a,b = r.split("(")[1].split(")")[0].split(",")
    a,b = int(a),int(b)
    sum += a*b
print(sum)

# b
# Find all instances of the string "mul(a,b)" where a and b are integers between 0 and 999 inclusive, OR 'do()' OR don't()

results = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)",s)

sum = 0
enabled = True
for r in results:
    if r[:3] == 'don':
        enabled = False
    elif r[:3] == 'do(':
        enabled = True
    if enabled and r[:3] == 'mul':
        a,b = r.split("(")[1].split(")")[0].split(",")
        a,b = int(a),int(b)
        sum += a*b
print(sum)