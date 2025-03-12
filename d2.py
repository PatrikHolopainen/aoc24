

# Read file test_input.txt thas has rows of numbers
# Store numbers as a list of lists of ints

with open('input.txt') as f:
    lines = f.readlines()
    data = [[int(x) for x in line.split()] for line in lines]

count = 0

diff_data = []

def diff(row):
    prev = row[0]
    diff_row = []
    for curr in row[1:]:
        diff_row.append(curr-prev)
        prev = curr
    return diff_row

for row in data:
    diff_data.append(diff(row))

for k,row in enumerate(diff_data[:]):
    if all([x in [-1,-2,-3] for x in row]) or all([x in [1,2,3] for x in row]):
        count += 1
    else:
        safe = False
        for i in range(len(data[k])):
            filtered_row = [x for j,x in enumerate(data[k]) if j != i]
            print(i,filtered_row)
            filtered_diff_row = diff(filtered_row)
            # print(filtered_diff_row)
            if all([x in [-1,-2,-3] for x in filtered_diff_row]) or all([x in [1,2,3] for x in filtered_diff_row]):
                safe = True
                print(f"Safe if you remove {i}")
        if safe:
            # print(data[k])
            count +=1

print(count)