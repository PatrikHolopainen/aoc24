
data = []
with open('input.txt') as f:
    l = f.readlines()
    for row in l:
        target, numbers = row.split(':')
        target = int(target)
        numbers = [int(x) for x in numbers.split()]
        data.append([target,numbers])

print(data)

result = 0

def find_solutions(row):
    target, numbers = row
    
    i = 0 # We move slot index later
    
    def inner(curr_total,remaining_numbers,target):
        if curr_total > target:
            return False
        if remaining_numbers == []:
            return curr_total == target
        
        return inner(curr_total+remaining_numbers[0],remaining_numbers[1:],target) or inner(curr_total*remaining_numbers[0],remaining_numbers[1:],target) or \
            inner(int(str(curr_total)+str(remaining_numbers[0])),remaining_numbers[1:],target)
    
    if inner(numbers[0],numbers[1:],target):
        print("Found solution for",row)
        return target
    else:
        return 0

for row in data:
    result += find_solutions(row)

print(result)